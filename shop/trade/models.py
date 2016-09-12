from django.db import models
from django.contrib.auth.models import User
from restaurants.models import Restaurant,Food
# Create your models here.

class Buyer_data(models.Model):
	name=models.CharField(max_length=50)
	phone=models.CharField(max_length=20)
	user=models.ForeignKey(User)


class Recode_code(models.Model):
	status=models.CharField(max_length=20)
	restaurant=models.ForeignKey(Restaurant)
	buyer=models.ForeignKey(Buyer_data)

class Recode_data(models.Model):
	food=models.ForeignKey(Food)
	number=models.DecimalField(max_digits=5,decimal_places=0)
	recode=models.ForeignKey(Recode_code)

