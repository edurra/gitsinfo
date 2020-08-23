from django.shortcuts import render
import gitsinfoapp.scripts.Gitsmain as gitsmain
import os
from gitsinfoapp.models import Repository, Finding
from django.utils import timezone
from datetime import datetime

def saveFindings(findings, repo):
	r = Repository.objects.filter(name=repo)
	if len(r) > 0:
		rep = r[0]
		f = Finding.objects.filter(repository = r[0].id)
		f_l_dict = list(f.values())
		f_vals = [x['finding'] for x in f_l_dict]
		for finding in findings:
			if finding not in f_vals:
				rep.finding_set.create(finding=finding, date = timezone.now())
				
		for f in f_vals:
			if f not in findings:
				old_finding = Finding.objects.get(finding=f)
				old_finding.solved = True
				old_finding.save()
	else:
		rep = Repository(name = repo)
		rep.save()
		for finding in findings:
			rep.finding_set.create(finding=finding, date = timezone.now())
