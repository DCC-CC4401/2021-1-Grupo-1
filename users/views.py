from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.forms.models import model_to_dict

from posts.models import Post, PostImage
from users.forms import RegisterForm, ProfileEditPrivacyForm, ProfileEditPasswordForm
from users.models import Region, Comuna, User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


def get_comunas_view(request, region_id):
    """
    API View to obtain the "comunas" associated with a region.
    """
    if request.method == "GET":
        comunas = list(Comuna.objects.filter(region_id=region_id).values())
        return JsonResponse(comunas, safe=False)


def login_user_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        return render(request, "users/login.html")

    if request.method == "POST":
        email = request.POST['correo']
        password = request.POST['contrasena']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, "users/login.html", {'errores': ["Los datos ingresados no son correctos"]})


def register_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        form = RegisterForm()
        errores = ''
        return render(request, 'users/register.html', {'form': form, 'errores': errores})

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password'])
            login(request, new_user)
            return HttpResponseRedirect(reverse('home'))
        trad = {"first_name": "Nombre", "last_name": "Apellido", "email": "Email", "phone_number": "Telefono",
                "address": "Dirección", "comuna": "Comuna", "password": "Contraseña", "region": "Región",
                "birth_date": "Fecha de nacimiento"}
        errors = ["Las siguientes cosas fallaron", '']
        form_errors = form.errors.as_data()
        for i in form_errors:
            errors += [trad[str(i)] + ': ' + str(form_errors[i][0].message)]
        return render(request, 'users/register.html', {'form': form, 'errores': errors})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def profile_view(request, user_id):
    if request.method == "GET":
        profile_user = User.objects.get(pk=user_id)
        queryset = Post.objects.select_related().filter(author=user_id)
        images = []
        for p in queryset:
            photo = PostImage.objects.filter(post_id=p.id).first()
            images.append(photo)
        zipped = zip(queryset, images)
        return render(request, 'users/profile_view.html',
                      {'profile_user': profile_user, 'posts': zipped})


@login_required
def profile_edit(request, user_id):
    if request.user.id != user_id:
        return HttpResponseForbidden()
    profile_user = request.user
    initial = model_to_dict(profile_user)  # Add user info as initial
    initial['region'] = profile_user.comuna.region_id
    privacy_form = ProfileEditPrivacyForm(initial=initial)
    password_form = ProfileEditPasswordForm(profile_user=profile_user)
    if request.method == "GET":
        return render(request, 'users/profile_edit.html', {'profile_user': profile_user,
                                                           'privacy_form': privacy_form,
                                                           'password_form': password_form})
    elif request.method == "POST":
        # Find out which form was submitted
        if 'submit-privacy-form' in request.POST:
            privacy_form = ProfileEditPrivacyForm(request.POST, instance=profile_user)
            if privacy_form.is_valid():
                privacy_form.save()
                return HttpResponseRedirect(reverse('profile', args=[user_id]))
            return render(request, 'users/profile_edit.html', {'profile_user': profile_user,
                                                               'privacy_form': privacy_form,
                                                               'password_form': password_form})
        elif 'submit-password-form' in request.POST:
            password_form = ProfileEditPasswordForm(request.POST, profile_user=profile_user)
            if password_form.is_valid():
                profile_user.set_password(password_form.cleaned_data['new_password'])
                profile_user.save()
                # Django will log out the user after password change. To avoid this,
                # we update the user's auth hash.
                update_session_auth_hash(request, profile_user)
                return HttpResponseRedirect(reverse('profile', args=[user_id]))
            return render(request, 'users/profile_edit.html', {'profile_user': profile_user,
                                                               'privacy_form': privacy_form,
                                                               'password_form': password_form})
