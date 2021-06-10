from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def create_post_view(request):
    return render(request, "posts/create_post.html")
