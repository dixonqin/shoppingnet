from django import forms

class GoodsForm(forms.Form):
	number = forms.IntegerField()