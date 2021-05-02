from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import UpdateView

from users.forms import RegisterForm
from users.models import Region, Comuna, User
from django.contrib.auth import authenticate, login, logout


def get_comunas_view(request, region_id):
    """
    API View to obtain the "comunas" associated with a region.
    """
    if request.method == "GET":
        comunas = list(Comuna.objects.filter(region_id=region_id).values())
        return JsonResponse(comunas, safe=False)


def login_user_view(request):
    if request.method == "GET":
        return render(request, "users/login.html")

    if request.method == "POST":
        email = request.POST['correo']
        password = request.POST['contrasena']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('')
        else:
            return HttpResponseRedirect('/login')


def register_view(request):
    # TODO: Create account on form.is_valid
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            return HttpResponseRedirect('/')


def profile_view(request, user_id):
    if request.method == "GET":
        profile_user = User.objects.get(pk=user_id)
        return render(request, 'users/profile_view.html', {'profile_user': profile_user})


class ProfileEditView(UpdateView):
    model = User
    context_object_name = 'profile_user'
    template_name = 'users/profile_edit.html'
    success_url = ''
    fields = [
        'first_name', 'last_name', 'phone_number', 'address', 'region', 'comuna', 'description',
    ]

    def get_object(self, queryset=None):
        pk = self.kwargs['user_id']
        return User.objects.get(pk=pk)

