from django import forms
from posts.models import Post, PostImage
from users.models import Comuna, Region
from datetime import date

MONTHS = {
    1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
    5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
    9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
}


class PostForm(forms.ModelForm):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label='Selecciona una opción')
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), empty_label='Selecciona una opción')
    fecha = forms.DateField(widget=forms.DateInput(attrs={"style": "display: none;"}))

    class Meta:
        model = Post
        fields = ['specie', 'pet_name', 'comuna',
                  'description', 'breed', 'sex', 'pet_size',
                  'parasytes', 'sterilized', 'vaccinated', 'status',
                  'sighting_date', 'region']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        if hasattr(self, 'instance'):
            # Initially, the comuna queryset is empty because the user has to first select a region.
            self.fields['comuna'].queryset = Comuna.objects.none()

    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
        return post


class ImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"style": "display: none;"}))

    class Meta:
        model = PostImage
        fields = ['image']


