from django.db import models

# Create your models here
class Country(models.Model):
	name = models.CharField(max_length=200)
	code = models.CharField(max_length=3)
	time_zone = models.CharField(max_length=20)
	isd_code = models.IntegerField()

	def __str__(self):
		return self.name

class State(models.Model):
	name = models.CharField(max_length=200)
	country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True)

	def __str__(self):
		return self.name

class Company(models.Model):
	name = models.CharField(max_length=200)
	start_date = models.DateTimeField("Company Start")
	country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=False)
	state = models.ForeignKey(State, on_delete=models.PROTECT, null=True)
	is_active = models.BooleanField()

	def __str__(self):
		return self.name


