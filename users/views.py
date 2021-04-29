from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponseRedirect

from users.forms import RegisterForm
from users.models import Region, Comuna
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


class HomepageView(View):

    def get(self, request):
        return render(request, "users/homepage.html")


class ResultsView(View):

    def get(self, request):
        return render(request, "users/results.html")