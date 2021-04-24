from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponseRedirect
from users.models import Region, Comuna
from django.contrib.auth import authenticate, login, logout


class GetComunas(View):
    """
    API View to obtain the "comunas" associated with a region.
    """

    def get(self, request, region_id):
        comunas = list(Comuna.objects.filter(region_id=region_id).values())
        return JsonResponse(comunas, safe=False)


def login_user(request):
    if request.method == 'GET':
        return render(request, "adoptapp/login.html")
    if request.method == 'POST':
        email = request.POST['correo']
        password = request.POST['contrasena']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('')
        else:
            return HttpResponseRedirect('/login')
