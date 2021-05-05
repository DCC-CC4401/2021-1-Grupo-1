from django import forms
from users.models import User, Region, Comuna
from datetime import date

MONTHS = {
    1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
    5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
    9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
}


class RegisterForm(forms.ModelForm):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label='Selecciona una opción')
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), empty_label='Selecciona una opción')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Año", "Mes", "Día"),
        years=range(date.today().year, 1900, -1),
        months=MONTHS
    ))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number',
                  'address', 'region', 'comuna', 'description',
                  'password', 'birth_date']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'ejemplo@dominio.com'
        self.fields['phone_number'].widget.attrs['placeholder'] = '+56912345678'
        if hasattr(self, 'instance'):
            # Initially, the comuna queryset is empty because the user has to first select a region.
            self.fields['comuna'].queryset = Comuna.objects.none()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ProfileEditForm(forms.ModelForm):
    # Add region field and change region-comuna default empty_label
    region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label='Selecciona una opción')

    def __init__(self, *args, **kwargs):
        # We override init to initially populate comuna queryset with the comunas that are
        # related to the user's region (otherwise, all comunas are listed in the <select> field).
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        if hasattr(self, 'instance'):
            self.fields['comuna'].queryset = Comuna.objects.filter(region__id=self.instance.comuna.region.id)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'phone_number', 'address', 'region', 'comuna', 'description',
        ]
