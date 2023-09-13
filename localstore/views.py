from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

import datetime

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(TemplateView):
	logger.warning('Homepage was accessed at '+str(datetime.datetime.now())+' hours!')
	template_name = "index.html"

@login_required
def CreateCompanyView(request):
	template_name = "portfolio-details.html"