from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def header(request):
    doc_base = loader.get_template('base-authentication.html')
    documento = doc_base.render()
    return HttpResponse(documento)
