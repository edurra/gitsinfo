from django.shortcuts import render
import gitsinfoapp.scripts.Gitsmain as gitsmain
import os
from gitsinfoapp.models import Repository, Finding
from django.utils import timezone
from datetime import datetime
from gitsinfoapp.scripts.Functions import saveFindings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect


@login_required(redirect_field_name='/login')
def index(request):
	context = {}
	if request.method == 'POST':
		repo = request.POST['repo']
		findings = gitsmain.findings(repo)
		if len(findings) == 0:
			saveFindings(findings, repo)
			findings = ['No sensitive data found in the repository']
		elif len(findings) == 1 and findings[0] == "Repository not found":
			findings = ["Repository not found"]
		else:
			saveFindings(findings, repo)
		context['findings'] = findings
	
	return render(request, 'gitsinfoapp/index.html', context)

@login_required(redirect_field_name='/login')
def history(request):
	context = {}
	history = []
	repositories = list(Repository.objects.values())
	if request.GET.get('repo'):
		repo = request.GET['repo']
		r = Repository.objects.filter(name=repo)
		if (len(r) >  0):
			f = Finding.objects.filter(repository = r[0].id)
			f_l_dict = list(f.values())
			history = [] 
			history = [(x['finding'], x['date'].strftime("%d %b %Y "), x['solved']) for x in f_l_dict]
			if len(history) == 0:
				history = [('No sensitive data found so far','','')]
		else:
			history = [("Repository not found","","")]
	
	context['history'] = history
	context['repositories'] = repositories
	return render(request, 'gitsinfoapp/history.html', context)

def loginuser(request):
	context = {}
	if request.method == 'GET':

		return render(request, 'gitsinfoapp/login.html', context)
	if request.method == 'POST':
		username = request.POST['user']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return render(request, 'gitsinfoapp/history.html', context)
		else:
			return render(request, 'gitsinfoapp/login.html', context)

def logoutuser(request):
	context = {}
	logout(request)
	return HttpResponseRedirect('/login/')

