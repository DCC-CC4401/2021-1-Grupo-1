from django.forms import formset_factory
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from posts.forms import PostForm, ImageForm
from posts.models import Post, PostImage, Interested


def post_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(pk=post_id)
        images = PostImage.objects.filter(post_id=post_id)
        interested = Interested.objects.filter(post_id=post_id)
        image_urls = [x.image.url for x in images]
        interested_users = [[x.user, x.date] for x in interested]
        return render(request, 'posts/post.html', {'post': post,
                                                       'image_urls': image_urls,
                                                       'interested_users': interested_users})


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

        trad = {'specie': 'Especie', 'pet_name': 'Nombre de la mascota', 'comuna': 'Comuna',
                'description': 'Descripción', 'breed': 'Raza', 'sex': 'Sexo', 'pet_size': 'Tamaño según su especie',
                'parasytes': 'Está desparasitado', 'sterilized': 'Está esterilizad', 'vaccinated': 'Está vacunado',
                'status': "Estado del animal",
                'sighting_date': 'Fecha del avistamiento'}
        errors = ["Las siguientes cosas fallaron", '']
        form_errors = form.errors.as_data()
        for i in form_errors:
            errors += [trad[str(i)] + ': ' + str(form_errors[i][0].message)]
        return render(request, "posts/create_post.html", {'form': form, 'image_form': formset, 'errores': errors})


def interested_api(request, user_id, post_id):
    if request.method == 'GET':
        if Interested.objects.filter(user_id=user_id, post_id=post_id).exists():
            return HttpResponse(status=200)  # OK, exists
        else:
            return HttpResponse(status=404)  # Not found
    elif request.method == 'PUT':
        if Interested.objects.filter(user_id=user_id, post_id=post_id).exists():
            return HttpResponse(status=200)  # OK (already exists)
        new_interested = Interested(user_id=user_id, post_id=post_id)
        new_interested.save()
        return HttpResponse(status=201)  # Created
    elif request.method == 'DELETE':
        if not Interested.objects.filter(user_id=user_id, post_id=post_id).exists():
            return HttpResponse(status=404)  # Not found
        Interested.objects.get(user_id=user_id, post_id=post_id).delete()
        return HttpResponse(status=200)  # OK
