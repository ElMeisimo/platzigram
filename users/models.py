from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kingdom(models.Model):
	"""Country Model"""
	name = models.CharField(max_length=100)

class City(models.Model):
	"""City Model"""
	name	= models.CharField(max_length=100)
	kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)

	def __init__(self, name, kingdom):
		if not isinstance(kingdom, Kingdom):
			kingdom = Kingdom.objects.get(name = kingdom)
		models.Model.__init__(self, name = name, kingdom = kingdom )

class Someone(models.Model):
	"""Someone Model."""
	bio     = models.TextField( blank = True )
	website = models.URLField(max_length = 200, blank = True)
	picture = models.ImageField(
		upload_to = 'users/pictures',
		blank     = True,
		null      = True)
	user     = models.OneToOneField(User, on_delete = models.CASCADE)
	city     = models.ForeignKey(City,on_delete = models.CASCADE)
	created  = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	def __init__(self, bio, website, picture, user, city):
		if not isinstance(city, City):
			city = City.objects.get(name = city)
		if not isinstance(user, User):
			user = User.objects.get(username = user)
		models.Model.__init__(
			self,
			bio 	= bio, 
			website = website, 
			picture = picture, 
			user 	= user, 
			city 	= city,
		)