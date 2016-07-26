from django import forms
from django.forms import ModelForm
from registration.forms import RegistrationForm
from customauth.models import MyUser
from shopping.models import Goods
from django.utils.translation import ugettext_lazy as _

class MyCustomUserForm(RegistrationForm):
    class Meta:
        model = MyUser
        fields = ['email', 'is_shop']

class GoodsForm(forms.Form):
	number = forms.IntegerField()



# shop = models.ForeignKey(Shop, on_delete = models.CASCADE)
# 	#以下商品信息，店主无法直接修改
# 	name = models.CharField(max_length = 30)
# 	category = models.CharField(max_length = 20)
# 	description = models.CharField(max_length = 200)
# 	price = models.IntegerField(default = 0)
# 	number = models.IntegerField(default = 0)
# 	#以下信息，店主无法修改
# 	rating = models.IntegerField(default = 5, max_value = 5, min_value = 1, editable = 'false')
# 	rating_number = models.IntegerField(default = 0, editable = 'false')

class ManageGoodsForm(forms.ModelForm):
	class Meta:
		model = Goods
		exclude = ['shop']
		labels = {
			'name':_("名称"),
			'category':_("类别"),
			'description':_("描述"),
			'price':_("价格"),
			'number':_("数量"),
			'sold_number':_("销量"),
			'rating':_("评价"),
			'rating_number':_("评价数"),
		}
		# help_texts = {
		# 	'name':_("名称"),
		# 	'category':_(""),
		# 	'description':_(""),
		# 	'price':_(""),
		# 	'number':_(""),
		# 	'rating':_(""),
		# 	'rating_numbera':_(""),
		# }
		# error_messages = {

		# }

