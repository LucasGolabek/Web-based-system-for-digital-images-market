from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class AddImageForm():
    usage_possibilities = (('P', 'Prywatne'), ('K', 'Komercyjne'), ('KO', 'Komercyjne ograniczone'))

    photo_name = forms.CharField(label='Nazwa zdjęcia', max_length=50)
    username = forms.CharField(label='Twoja nazwa użytkownika', max_length=100)
    description = forms.CharField(label='Opis zdjęcia', max_length=600)
    price = forms.FloatField()
    usage = forms.CharField(max_length=2, choices=usage_possibilities)
