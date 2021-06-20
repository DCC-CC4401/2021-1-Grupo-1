from django.forms import formset_factory
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from posts.forms import PostForm, ImageForm


def post_view(request, post_id):
    if request.method == "GET":
        post_info = Post.objects.get(pk=post_id)
        return render(request, 'posts/post.html', {'post_info': post_info})


def create_post_view(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden(status=403)
    image_formset = formset_factory(ImageForm, extra=4, max_num=4)
    if request.method == "GET":
        form = PostForm()
        formset = image_formset()
        return render(request, "posts/create_post.html", {'form': form, 'image_form': formset})

    if request.method == "POST":
        form = PostForm(request.POST)
        formset = image_formset(request.POST)
        if form.is_valid():
            #Aquí se agrega el usuario al post
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            for image_form in formset:
                if image_form.is_valid():
                    img = image_form.save(commit=False)
                    img.post = post
                    img.save()
            return HttpResponseRedirect(reverse('home'))  # tiene que redirigir al post
