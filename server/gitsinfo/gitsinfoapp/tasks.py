from __future__ import absolute_import
from celery import shared_task
from gitsinfoapp.models import Repository, Finding
import random
@shared_task
def add():
	ran = random.random()
	r = Repository(name = str(ran))
	r.save()
	print("Repository:")
	print(r)
	print("All repositories")
	print(Repository.objects.all())
