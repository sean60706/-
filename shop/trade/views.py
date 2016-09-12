from django.shortcuts import render_to_response
from django.contrib.auth.models import User,Permission
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from restaurants.models import Restaurant,Food
from trade.models import Buyer_data


def buyer_data(request):
	
	
	current_user=request.user
	id=current_user.id
	user=User.objects.get(id=id)
	data=Buyer_data.objects.get(user=user)
	

	name=data.name
	phone=data.phone


	new_name=request.POST.get('new_name',False)
	new_phone=request.POST.get('new_phone',False)

	if new_name is not False and new_phone is not False:
		data.name=new_name
		data.phone=new_phone
		data.save()
		return HttpResponseRedirect('/index/')

	return render_to_response('buyer_data.html',RequestContext(request,locals()))

def search(request):
	_name=request.POST.get('new_name','')
	_id=request.POST.get('new_id','')
	#_time=request.POST.get('time','')
	restaurants=Restaurant.objects.all()
	
	if _id is not '':
		restaurants=Restaurant.objects.get(id=_id)
	else:
		if _name is not '':
			restaurants=Restaurant.objects.filter(name__contains=_name)
		else:
			restaurants=Restaurant.objects.all()
	return render_to_response('search.html',RequestContext(request,locals()))

def shop_info(request,id):
	user=User.objects.get(id=id)
	restaurant=Restaurant.objects.get(owner=user)

	return render_to_response('shop_info.html',locals())

def menu(request,id):
	if not request.user.is_authenticated():	
		return HttpResponseRedirect('/accounts/login/?next={0}'.format(request.path))

	if not request.user.has_perm('have_shop'):
		return render_to_response('menu.html',locals())


	n='/shop_info/'+str(id)
	return HttpResponseRedirect(n)