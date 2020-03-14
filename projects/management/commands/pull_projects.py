import requests
import json
import arrow

from django.core.management.base import BaseCommand, CommandError

from ...models.models import Project

class Command(BaseCommand):

	def handle(self, *args, **options):
		r = requests.get("https://api.github.com/users/jlchilders11/repos")
		data = json.loads(r.text)

		for repo in data:
			Project.objects.update_or_create(
				github_id=repo['id'],
				defaults={
					'title':repo['name'].replace("-"," "),
					'last_update':arrow.get(repo['updated_at']).datetime,
					'read_me':repo['description'],
					'url':repo['html_url'],
				}
			)

		self.stdout.write(self.style.SUCCESS(data[0]['id']))