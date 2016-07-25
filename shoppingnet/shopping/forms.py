from django import forms
from registration.forms import RegistrationForm
from customauth.models import MyUser

class MyCustomUserForm(RegistrationForm):
    class Meta:
        model = MyUser
        fields = ['email', 'is_shop']

class GoodsForm(forms.Form):
	number = forms.IntegerField()