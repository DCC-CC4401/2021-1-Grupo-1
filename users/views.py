from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse

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
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        return render(request, "users/login.html")

    if request.method == "POST":
        email = request.POST['correo']
        password = request.POST['contrasena']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('home'))


def register_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

