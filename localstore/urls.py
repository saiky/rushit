from django.urls import path


from localstore import views

from . import views

urlpatterns = [
	path('', views.IndexView.as_view(), name="index"),
	
	path('localstore/create', views.CreateCompanyView, name="localstore_create"),
]