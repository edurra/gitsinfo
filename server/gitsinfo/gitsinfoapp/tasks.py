from __future__ import absolute_import
from celery import shared_task
from gitsinfoapp.models import Repository, Finding
import gitsinfoapp.scripts.Gitsmain as gitsmain
from gitsinfoapp.scripts.Functions import saveFindings
import random
@shared_task
def periodicscan():
	repositories = Repository.objects.filter(periodicscan=True)
	repos = repositories.values()
	for repo_dic in repos:
		repo = repo_dic["name"]
		print("Scanning repository: " + repo)
		findings = gitsmain.findings(repo)
		if len(findings)!= 1 or (len(findings) == 1 and findings[0] != "Repository not found"):
			saveFindings(findings, repo)
