from django import forms
from .models import OrderForm
class GoodsForm(forms.ModelForm):
	class Meta:
		model = OrderForm
		fields = ('number',)