from django.db import models

# Create your models here.

class Kingdom(models.Model):
	"""Country Model"""
	name = models.CharField(max_length=100)

class City(models.Model):
	"""City Model"""
	name    = models.CharField(max_length=100)
	kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)

	def __init__(self, name, kingdom):
		if not isinstance(kingdom, Kingdom):
			kingdom = Kingdom.objects.get(name = kingdom)
		models.Model.__init__(self, name = name, kingdom = kingdom )

class User(models.Model):
	"""User Model"""
	email      = models.EmailField(unique=True)
	password   = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name  = models.CharField(max_length=100)
	bio        = models.TextField(blank=True)
	super_user = models.BooleanField(default=False)
	birthday   = models.DateField(blank=True, null=True)
	created    = models.DateTimeField(auto_now_add=True)
	modified   = models.DateTimeField(auto_now=True)
	city       = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)

	def __init__(self, email, password, first_name, 
		last_name, bio, super_user, birthday, created, modified, city):
		if not isinstance(city, City):
			city = City.objects.get(name = city)
		models.Model.__init__(
			self,
			email      = email,
			password   = password,
			first_name = first_name,
			last_name  = last_name,
			bio        = bio,
			super_user = super_user,
			birthday   = birthday,
			created    = created,
			modified   = modified,
			city       = city
		)