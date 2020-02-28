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
				title=repo['name'],
				last_update=arrow.get(repo['updated_at']).date(),
				read_me=repo['description'],
				url=repo['html_url'],
				github_id=repo['id']
			)

		self.stdout.write(self.style.SUCCESS(data[0]['id']))