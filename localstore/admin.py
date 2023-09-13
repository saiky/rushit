from django.contrib import admin

# Register your models here.
from localstore.models import Country, State, Company

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
	pass

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
	pass

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	pass
