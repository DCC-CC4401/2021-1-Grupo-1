from django import forms
from django.core.exceptions import ValidationError

from users.models import User, Region, Comuna


class RegisterForm(forms.ModelForm):
    # Remove empty labels (ugly "--------")
    region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label=None)
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), empty_label=None)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number',
                  'address', 'region', 'comuna', 'description',
                  'birth_date', 'password']

    def clean_birth_date(self):
        raise ValidationError(('No birth date'), code='missing')
