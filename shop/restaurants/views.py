from django.shortcuts import render_to_response
from django.contrib.auth.models import User,Permission
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from restaurants.models import Restaurant,Food

def delete_menu(request,food_id):
	f=Food.objects.get(id=food_id)
	f.delete()
	return render_to_response('index.html',RequestContext(request,locals()))

def manage_menu(request):
	current_user=request.user
	id=current_user.id
	u=User.objects.get(id=id)
	restaurant=Restaurant.objects.get(owner=u)
	return render_to_response('manage_menu.html',RequestContext(request,locals()))


def manage_menu_data(request,food_id):
	f=Food.objects.get(id=food_id)
	name=f.name
	price=f.price
	comment=f.comment
	ingredient=f.ingredient

	new_name=request.POST.get('new_name',False)
	new_price=request.POST.get('new_price',False)
	new_comment=request.POST.get('new_comment',False)
	new_ingredient=request.POST.get('new_ingredient',False)

	if new_name is not False:
		f.name=new_name
		f.price=new_price
		f.comment=new_comment
		f.ingredient=new_ingredient
		f.save()

	return render_to_response('manage_menu_data.html',RequestContext(request,locals()))
	#render_to_response('manage_menu_data.html',RequestContext(locals()))

def new_menu(request):
	current_user=request.user
	id=current_user.id
	u=User.objects.get(id=id)
	restaurant=Restaurant.objects.get(owner=u)
	

	name=request.POST.get('name',False)
	price=request.POST.get('price',0)
	ingredient=request.POST.get('ingredient',False)
	comment=request.POST.get('comment',False)

	if name is not False and price is not 0 and ingredient is not False and comment is not False:
		f=Food.objects.create(name=name,price=price,ingredient=ingredient,comment=comment,restaurant=restaurant)
	


	return render_to_response('new_menu.html',RequestContext(request,locals()))


def manage_information(request):
	current_user=request.user
	id=current_user.id
	user=User.objects.get(id=id)
	r=Restaurant.objects.get(owner=user)

	errors=[]
	
	name=r.name
	photo=r.photo
	address=r.address
	category=r.category
	operating_time=r.operating_time
	area=r.area
	introduction=r.introduction
	
	
	new_name=request.POST.get('name','false')
	new_photo=request.POST.get('photo','false')
	new_address=request.POST.get('address','false')
	new_category=request.POST.get('category','false')
	new_operating_time=request.POST.get('operating_time','false')
	new_area=request.POST.get('area','false')
	new_introduction=request.POST.get('introduction','false')

	error=any(not request.POST[k] for k in request.POST)
	if any(not request.POST[k] for k in request.POST):
			errors.append('有空白欄位，請重新輸入')
	

	#if 	new_name is not 'false' 	and 	
	#	new_photo is not 'false'	and
	#	new_address is not 'false'	and
	#	new_category is not 'false'	and
	#	new_operating_time is ont 'false' and
	#	new_area	is not 'false'	and
	#	new_introduction is not 'false':
	
	if 	new_name is not 'false' and not errors:
		r.name=new_name
		r.photo=new_photo
		r.address=new_address	
		r.category=new_category
		r.operating_time=new_operating_time
		r.area=new_area
		r.introduction=new_introduction
		r.save()
		return HttpResponseRedirect('/index/')
	'''if not errors:
			r.name=new_name
			r.photo=new_photo
			r.address=new_address	
			r.category=new_category
			r.operating_time=new_operating_time
			r.area=new_area
			r.introduction=new_introduction
			r.save()
	'''
			#return render_to_response('index.html',RequestContext(request,locals()))
	

	return render_to_response('manage.html',RequestContext(request,locals()))
	




'''
工作進度:
目前已經將id掛上url了，接下來將進行店家資料的編輯以及上菜單

這些做完之後就可以開始買方的功能了


'''