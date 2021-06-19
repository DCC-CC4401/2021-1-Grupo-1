from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from posts.forms import PostForm


# Create your views here.
def create_post_view(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            form = PostForm()
            return render(request, "posts/create_post.html", {'form': form})

        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                new_post = ''  # no sé que poner aqui uwu
                return HttpResponseRedirect(reverse('home'))
    else:
        # Aquí se puede redirigir a una página de error quizás, por el momento esta igual que el if para trabajar
        if request.method == "GET":
            form = PostForm()
            return render(request, "posts/create_post.html", {'form': form})

        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                new_post = ''  # no sé que poner aqui uwu
                return HttpResponseRedirect(reverse('home'))
