from django.forms import formset_factory
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse

from posts.forms import PostForm, ImageForm


# Create your views here.
def create_post_view(request):
    # if not request.user.is_authenticated:
    #   return HttpResponseForbidden(status=403)
    if request.method == "GET":
        form = PostForm()
        image_formset = formset_factory(ImageForm, extra=4, max_num=4)
        formset = image_formset()
        return render(request, "posts/create_post.html", {'form': form, 'image_form': formset})

    if request.method == "POST":
        files = request.FILES.getlist('image')
        form = PostForm(request.POST)
        if form.is_valid():
            for f in files:
                pass  # Setear que corresponda a cada post
            form.save()
            new_post = ''  # no sé que poner aqui uwu
            return HttpResponseRedirect(reverse('home'))  # tiene que redirigir al post
