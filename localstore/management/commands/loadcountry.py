from django.core.management.base import BaseCommand
from localstore.models import Country 
import json


class Command(BaseCommand):

	def add_argument(self, parser):
		parser.add_arguments('--option', default='default', help='Option 1')

	def handle(self, *args, **options):
		with open("C:\\projects\\djapp\\rushit\\static\\country_lists.json", 'r') as f:
			jcounty_obj = json.load(f)
			for country_js in jcounty_obj['countries']:
				if not Country.objects.filter(code=country_js['code']):
					isd_code = int(country_js['isd_code'][1:])
					time_zone = country_js['utc_offset'].split('to')
					country_obj = Country(name=country_js['name'], code=country_js['code'], time_zone=time_zone[0], isd_code=isd_code)
					country_obj.save()

			#print(jcounty_obj['countries'])
		done = True
		if done:
			self.stdout.write(self.style.SUCCESS('Import Success'))
		else:
			self.stdout.write(self.style.FAILURE('Impot Fail'))
