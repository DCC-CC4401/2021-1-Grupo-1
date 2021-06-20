from django import forms
from posts.models import Post, PostImage
from users.models import Comuna
from datetime import date

MONTHS = {
    1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
    5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
    9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
}


class PostForm(forms.ModelForm):
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), empty_label='Selecciona una opción')

    class Meta:
        model = Post
        fields = ['specie', 'pet_name', 'author', 'comuna',
                  'description', 'breed', 'sex', 'pet_size',
                  'parasytes', 'sterilized', 'vaccinated', 'status',
                  'sighting_date']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
        return post


class ImageForm(forms.Form):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"style": "display: none;"}))

    def save(self, commit=True):
        image_post = super().save(commit=False)
        if commit:
            image_post.save()
        return image_post
