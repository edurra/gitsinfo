import sys
import gitsinfoapp.scripts.Gitsfunctions as Gitsfunctions
import os
import git
import shutil

ALLOWED_EXTENSIONS = ["txt","php","py","html","js","sh","jsp", "json", "xml"]
def findings(path):
	sensitive_info = []
	try:
		if os.path.exists(os.getcwd() + '/tmp'):
			shutil.rmtree(os.getcwd() + '/tmp')
		os.mkdir(os.getcwd() + '/tmp')
		git.Git(os.getcwd() + '/tmp').clone(path)
		rootdir = os.getcwd() + '/tmp'
		for subdir, dirs, files in os.walk(rootdir):
			for f1 in files:
				filepath = os.path.join(subdir, f1)
				file_split = f1.split(".")
				extension = file_split[len(file_split)-1]
				if extension in ALLOWED_EXTENSIONS:
					f = open(filepath, 'r', encoding = "latin-1")
					lines = f.readlines()
					f.close()
					name = filepath.replace(os.getcwd() + '/tmp','')
					ftocheck = Gitsfunctions.FileToCheck(lines,name)
					file_info = ftocheck.discoverSecrets()
					if len(file_info) > 0:
						for inf in file_info:
							sensitive_info.append(inf)
	except:
		sensitive_info.append("Repository not found")
	shutil.rmtree(os.getcwd() + '/tmp')
	return sensitive_info


