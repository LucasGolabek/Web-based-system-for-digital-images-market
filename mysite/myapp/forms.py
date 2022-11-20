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
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))

    class Meta:
        model = Product
        fields = ['name', 'username', 'description', 'price', 'usage', 'image']

    def __init__(self, *args, **kwargs):
        super(AddImageForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['usage'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'


class BuyoutProposalForm(ModelForm):
    user_from = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    user_to = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))


    class Meta:
        model = Messages
        fields = ['user_from', 'user_to', 'message_text', 'negotiation_price', 'negotiation_usage', 'photo_id']


    def __init__(self, *args, **kwargs):
        super(BuyoutProposalForm, self).__init__(*args, **kwargs)

        self.fields['photo_id'].widget.attrs['hidden'] = 'hidden'
        self.fields['message_text'].widget.attrs['class'] = 'form-control'
        self.fields['negotiation_price'].widget.attrs['class'] = 'form-control'
        self.fields['negotiation_usage'].widget.attrs['class'] = 'form-control'




class EditForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'usage']

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['usage'].widget.attrs['class'] = 'form-control'