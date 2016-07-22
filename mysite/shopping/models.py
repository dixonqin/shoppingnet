from django.db import models
#修改日志
#7/21 添加了除了Insert Delete QueryByXXX之外的所有接口，其中Shop中的goodsList和goodsListHis暂采用ForeignKey，是否使用列表储存两个表单有待商议，User中的几个表单同。User和Shop的Delete函数未实现。新创建OrderForm类，用于存储订单信息，User和Shop类都添加了OrderForm类的ForeignKey对象orderForms。新建了comment类，Goods中的comments用ForeignKey储存。另外因为类里面的每个变量前都会带一个类的大写符号，为防止以后错用，创建了所有变量的获取函数，命名方式为Get+变量名，如GetName、GetPassword，获取变量时尽量使用Get函数，每一个变量的更改也有对应的Modify函数，另外插入操作都是用New命名的插入函数。
#另注：Shop的Score需要先ComScore，OrderForm的总价需要调用ComTotalPrice计算，Goods的Score直接在调用NewComment时计算出来了。


# Create your models here.
class Shop(models.Model):
	SName = models.CharField(max_length = 30)
	SPassword = models.CharField(max_length = 30)
	SPayAccount = models.CharField(max_length = 30)
	SPayPassword = models.CharField(max_length = 30)
	SScore = models.IntegerField(default = 0)
	#goodsList = [] #用list存储物品列表，待商榷
	#goodsListHis = [] 
	#用于记录商铺出售过的物品,防止店家通过删除商品来刷评价
	SGoodsList = models.ForeignKey(Goods, on_delete = models.CASCADE)
	SGoodsListHis = models.ForeignKey(Goods, on_delete = models.CASCADE)
	#用于记录商铺出售过的物品,防止店家通过删除商品来刷评价
	SOrderForms = models.ForeignKey(OrderForm, on_delete = models.CASCADE)
	#Info
	SCategory = models.CharField(max_length = 30)
	SLocation = models.CharField(max_length = 30)
	SBrefIntro = models.CharField(max_length = 500)

	def GetName():
		return SName

	def GetPassWord():
		return SPassword

	def GetPayAccount():
		return SPayAccount

	def GetPayPassword():
		return SPayPassword

	def GetGoodList():
		return SGoodsList

	def GetGoodListHis():
		return SGoodsListHis

	def GetOrderForm():
		return SOrderForms

	def GetCategory():
		return SCategory

	def GetLocation():
		return SLocation

	def GetBrefIntro():
		return SBrefIntro

	def ModifyPassword(newPassword):
		SPassword = newPassword

	def ModifyPayInfo(newAccount,newPassword):
		SPayPassword = newPassword
		SPayAccount = newAccount

	def ModifyInfo(newInfo):
		SCategory = newInfo.SCategory
		SLocation = newInfo.SLocation
		SBrefIntro = newInfo.SBrefIntro

	def ComScore(): #对商铺出售过的所有物品的评价取平均，获取商铺评价
		temp = 0
		num = 0
		for SGoods in SGoodsListHis:
			temp += SGoods.GScore
			num += 1
		SScore = temp / num

	def GetScore(): #获取商铺评价
		return SScore

	def NewGoods(tarGoods):
		SGoodsList.append(tarGoods)
		SGoodsListHis.append(tarGoods)

	def OutGoods(tarGoods):
		SGoodsList.move(tarGoods)

	def IncreaseGoods(tarGoods, tnum):
		idx = SGoodsList.index(tarGoods)
		SGoodsList[idx].GNumber += tnum

	#def Delete():

	def GetOrderForm():
		return SOrderForms

	def NewOrderForm(tarOF):
		SOrderForms.append(tarOF)

	def ModifyGoods(tarGoods):#修改内容不包括comments和score，这两项不能由商铺进行修改
		idx = goodsList.index(tarGoods)
		goodsList[idx].copyGoods(tarGoods)

	class Meta:
		ordering = ["-name"]

	def __str__(self):
		return self.name

class User(models.Model):
	UImgUrl = models.CharField(max_length = 200)
	UName = models.CharField(max_length = 30)
	UEmail = models.EmailField()
	UPassword = models.CharField(max_length = 30)
	UAddress = models.CharField(max_length = 30)
	UPayAccount = models.CharField(max_length = 30)
	UPayPassword = models.CharField(max_length = 30)
	UOrderForms = models.ForeignKey(OrderForm, on_delete = models.CASCADE)
	shopHistory = models.ForeignKey(Shop, on_delete = models.CASCADE)
	goodsHistory = models.ForeignKey(Goods, on_delete = models.CASCADE)
	shoppingCart = models.ForeignKey(Goods, on_delete = models.CASCADE)
	
	def ModifyName(newName):
		UName = newName

	def GetName():
		return UName

	def ModifyEmail(newEmail):
		UEmail = newEmail

	def GetEmail():
		return UEmail

	def ModifyPassword(newPassword):
		UPassword = newPassword

	def GetPassWord():
		return UPassword

	def ModifyImg(newImgUrl):
		UImgUrl = newImgUrl

	def GetImg():
		return UImgUrl

	def ModifyPayInfo(newAccount, newPassword):
		UPayAccount = newAccount
		UPayPassword = newPassword

	def GetPayAccount():
		return UPayAccount

	def GetPayPassword():
		return UPayPassword

	def GetAddress():
		return UAddress

	#def Delete():

	def GetShoppingCart():
		return shoppingCart

	def InsertShoppingCart(newGoods):
		shoppingCart.append(newGoods)

	def ClearShoppingCart():
		for goods in shoppingCart:
			shoppingCart.move(goods)

	def GetGoodsHistory():
		return goodsHistory
	
	def GetShopHistory():
		return shopHistory

	def GetOrderForm():
		return UOrderForms

	def NewOrderForm(tarOF):
		UOrderForms.append(tarOF)

	def __str__(self):
		return self.name

class Goods(models.Model):
	GName = models.CharField(max_length = 30)
	#sell = models.ForeignKey(Shop, on_delete = models.CASCADE) #useless
	buy = models.ForeignKey(User, on_delete = models.CASCADE)
	GComments = models.ForeignKey(Comment, on_delete = models.CASCADE)
	GNumber = models.IntegerField(default = 0)
	GPrice = models.IntegerField(default = 0)
	GScore = models.IntegerField(default = 0)
	GShop = models.ForeignKey(Shop, on_delete = models.CASCADE)
	#info
	GCategory = models.CharField(max_length = 30)
	GBrefIntro = models.CharField(max_length = 500)
	GIntroHtml = models.CharField(max_length = 200)#详细介绍的网页跳转
	GImgUrls = models.CharField(max_length = 200)#简介中的图片
	GKeyWords = models.CharField(max_length = 30)

	def copyGoods(tarGoods):
		GName = tarGoods.GName
		#sell = tarGoods.sell
		buy = tarGoods.buy
		GNumber = tarGoods.GNumber
		GPrice = tarGoods.GPrice
		GScore = tarGoods.GScore
		GComments = tarGoods.GComments
		GCategory = tarGoods.GCategory
		GBrefIntro = tarGoods.GBrefIntro
		GIntroHtml = tarGoods.GIntroHtml
		GImgUrls = tarGoods.GImgUrls
		GKeyWords = tarGoods.GKeyWords
		GShop = tarGoods.GShop

	def NewComment(newComment):
		GComments.append(newComment)
		t = len(GComments)
		GScore = (1 - t) / t * GScore + 1 / t * newComment.CScore

	def ModifyInfo(newInfo):
		GCategory = newInfo.GCategory
		GBrefIntro = newInfo.GBrefIntro
		GIntroHtml = newInfo.GIntroHtml
		GImgUrls = newInfo.GImgUrls
		GKeyWords = newInfo.GKeyWords

	def GetName():
		return GName

	def GetNumber():
		return GNumber

	def GetPrice():
		return GPrice

	def GetCategory():
		return GCategory

	def GetBrefIntro():
		return GBrefIntro

	def GetImgUrls():
		return GImgUrls

	def GetIntroHtml():
		return GIntroHtml

	def GetKeyWords():
		return GKeyWords

	def GetShop():
		return GShop

	def GetComment():
		return GComments

	def GetScore():
		return GScore

	def __str__(self):
		return self.GName

class OrderForm(models.Model):
	ONum = models.IntegerField(default = 0)
	OrderId = models.IntegerField(default = 0)
	OShop = models.ForeignKey(Shop, on_delete = models.CASCADE)
	OGoods = models.ForeignKey(Goods, on_delete = models.CASCADE)
	OUser = models.ForeignKey(User, on_delete = models.CASCADE)
	OStatus = models.CharField(max_length = 30)
	OTotalPrice =models.IntegerField(default = 0)

	def copyOF(tarOF):
		OrderId = tarOF.OrderId
		OShop = tarOF.OShop
		OGoods = tarOF.OGoods
		OUser = tarOF.OUser
		OStatus = tarOF.OStatus
		ONum = tarOF.ONum
		OTotalPrice = tarOF.OTotalPrice

	def GetNum():
		return ONum

	def GetId():
		return OrderId

	def GetShop():
		return OShop

	def GetGoods():
		return OGoods

	def ModifyStatus(newStatus):
		OStatus = newStatus

	def GetStatus():
		return OStatus

	def ComTotalPrice():
		OTotalPrice = OGoods.GPrice * ONum

	def GetTotalPrice():
		return OTotalPrice

	def GetUser():
		return OUser



class Comment:
	CId = models.IntegerField(default = 0)
	CUser = models.ForeignKey(User, on_delete = models.CASCADE)
	CGoods = models.ForeignKey(Goods, on_delete = models.CASCADE)
	CContent = models.CharField(max_length = 300)
	CScore = models.IntegerField(default = 0)

	def copyComment(tarC):
		CId = tarC.CId
		CUser = tarC.CUser
		CGoods = tarC.CGoods
		CContent = tarC.CContent
		CScore = tarC.CScore

	def GetContent():
		return CContent

	def GetScore():
		return CScore

	def GetId():
		return CId

	def GetGoods():
		return CGoods

	def GetUser():
		return CUser
