from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
import requests
import json
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('how_many', nargs='+', type=int)

    def handle(self, *args, **options):
    	request = requests.get("https://randomuser.me/api/?format=json&inc=login,email&results="+str(options['how_many'][0]))
    		# ,data={'results':options["how_many"]})
    	result = json.loads(request.text).get("results")
    	for i in result:
    		User.objects.create_user(i['login']['username'],i['login']['password'],i['email'])
