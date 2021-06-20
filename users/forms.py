from django import forms
from django.core.exceptions import ValidationError

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
                  'address', 'comuna', 'description',
                  'password', 'birth_date']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'ejemplo@dominio.com'
        self.fields['phone_number'].widget.attrs['placeholder'] = '+56912345678'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ProfileEditPrivacyForm(forms.ModelForm):
    # Add region field and change region-comuna default empty_label
    region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label='Selecciona una opción')

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'phone_number', 'address', 'comuna', 'description',
        ]


class ProfileEditPasswordForm(forms.Form):
    current_password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    new_password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    new_password_repeat = forms.CharField(max_length=128, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        self.profile_user = kwargs.pop('profile_user')
        super(ProfileEditPasswordForm, self).__init__(*args, **kwargs)

    def clean(self):
        cur_pw = self.cleaned_data['current_password']
        pw1 = self.cleaned_data['new_password']
        pw2 = self.cleaned_data['new_password_repeat']
        if not self.profile_user.check_password(cur_pw):
            raise ValidationError('La contraseña actual ingresada es incorrecta.', code='invalid')
        if pw1 != pw2:
            raise ValidationError('Las contraseñas ingresadas no coinciden.', code='invalid')
