from django.contrib import admin
from users.models import City, Someone

# Register your models here.


# admin.site.register(Kingdom)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	search_fields = ['kingdom__name','name']
	list_display  = ('name', 'kingdom')
	ordering = ['kingdom__name','name']

@admin.register(Someone)
class SomeoneAdmin(admin.ModelAdmin):
	list_display = ('user', 'fullName', 'city', 'created')
	list_filter  = ('created', 'user__is_active')

	def fullName(self, someone):
		return "{f_name} {l_name}"\
			  .format(
					  f_name = someone.user.first_name,
					  l_name = someone.user.last_name
			  )
	fullName.short_description = "Name"