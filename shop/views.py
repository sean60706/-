from django.shortcuts import render_to_response
from django.contrib.auth.models import User,Permission
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from restaurants.models import Restaurant,Food
from trade.models import Buyer_data
#def index(request):
	#return HttpResponseRedirect('index.html')

def index(request):
	#user=User.objects.get(username=request.username)
	#perm=Permission.objects.get(codename='have_shop')
	#is_shop=user.has_perm('restaurants.have_shop')
	current_user=request.user
	id=current_user.id
	return render_to_response('index.html',RequestContext(request,locals()))
#def index(request):
	#return render_to_response('index.html',RequestContext(request,locals()))

def register(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST)
		visitor=request.POST['visitor']

		if form.is_valid():
			user=form.save()
			if visitor is 's':
				perm=Permission.objects.get(codename='have_shop')
				user.user_permissions.add(perm)
				r=Restaurant.objects.create(name='',photo='',address='',area='',operating_time='',introduction='',category='',owner=user)
			else:
				buyer=Buyer_data.objects.create(name='default',phone='0000',user=user)

			return HttpResponseRedirect('/accounts/login')
	else:
		form=UserCreationForm()
	return render_to_response('register.html',RequestContext(request,locals()))



def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/index/')

	username=request.POST.get('username','')
	password=request.POST.get('password','')

	user=auth.authenticate(username=username,password=password)
	#auth.authenticate用作登入，參數有兩個，帳號跟密碼
	path=request.path

	if user is not None and user.is_active:
		auth.login(request,user)
		#用於保持使用者的登入，使用session
		#link='/index/'+str(user.id)
		return HttpResponseRedirect('/index/')
	else:
		return render_to_response('login.html',RequestContext(request,locals()))

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/index/')
