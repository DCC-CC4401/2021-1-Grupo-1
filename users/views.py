from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from users.models import Region, Comuna



class GetComunas(View):
    """
    API View to obtain the "comunas" associated with a region.
    """

    def get(self, request, region_id):
        comunas = list(Comuna.objects.filter(region_id=region_id).values())
        return JsonResponse(comunas, safe=False)
