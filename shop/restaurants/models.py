from django.db import models
from django.contrib.auth.models import User

# Create your views here.
class Restaurant(models.Model):
	photo=models.CharField(max_length=1000)
	name=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	area=models.CharField(max_length=200)
	operating_time=models.CharField(max_length=50)
	introduction=models.CharField(max_length=200)
	category=models.CharField(max_length=200)
	owner=models.ForeignKey(User)
	class meta:
		permissions=(
			("have_shop","Have shop")
		)

class Food(models.Model):
	name=models.CharField(max_length=50)
	price=models.DecimalField(max_digits=4,decimal_places=0)
	ingredient=models.CharField(max_length=1000)
	comment=models.CharField(max_length=200)	
	restaurant=models.ForeignKey(Restaurant)
	

