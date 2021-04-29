from django.shortcuts import render
from django.views import View


class HomepageView(View):

    def get(self, request):
        return render(request, "adoptapp/homepage.html")


class ResultsView(View):

    def get(self, request):
        return render(request, "adoptapp/results.html")