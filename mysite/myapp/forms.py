from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Product, Messages


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


class AddImageForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'username', 'description', 'price', 'usage', 'image']

class BuyoutProposalForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['user_from', 'user_to', 'message_text', 'negotiation_price', 'negotiation_usage', 'photo_id']


