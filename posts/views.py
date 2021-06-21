from django.forms import formset_factory
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from posts.forms import PostForm, ImageForm
from posts.models import Post, PostImage


def post_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(pk=post_id)
        images = PostImage.objects.filter(post_id=post_id)
        image_urls = [x.image.url for x in images]
        return render(request, 'posts/post.html', {'post': post,
                                                   'image_urls': image_urls})


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
        formset = image_formset(request.POST, request.FILES)
        if form.is_valid():
            # Aquí se agrega el usuario al post
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            for image_form in formset:
                if image_form.is_valid():
                    img = image_form.save(commit=False)
                    img.post = post
                    if img.image:
                        img.save()
            return HttpResponseRedirect(reverse('post_view', args=[post.id]))  # tiene que redirigir al post
        return render(request, "posts/create_post.html", {'form': form, 'image_form': formset})
