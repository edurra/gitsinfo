
import re

class FileToCheck:
	def __init__(self, content, name):

		self.content = content
		self.sensitive_info = []
		self.name = name

		self.regex_api = [
						r'[1-9][0-9]+[0-9a-zA-Z]{40}', #Twitter
						r'[0-9a-zA-Z/+]{40}', #AWS Secret key
						r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', #Google Cloud
						r'[A-Za-z0-9_]{21}--[A-Za-z0-9_]{8}' #Google Cloud API Key
		]
		self.regex_cert = r"(-----BEGIN CERTIFICATE-----)"
		self.regex_token =  [
					r"Bearer: ?['\"][a-zA-Z1-9]{30,}",
					r"ey[a-zA-Z1-9]{40,}",
					r"key=.{25,}"								
		]


	def discoverSecrets(self):
		self.discoverKeys()
		self.discoverCertificates()
		self.discoverTokens()
		return self.sensitive_info

	def discoverKeys(self):
		i = 0
		for line in self.content:
			for regex in self.regex_api:
				search = re.search(regex, line)
				if search:
					self.sensitive_info.append("Possible API Key detected: " + search.group(0)[0:3] + "..." + " at file " + self.name + " (line " + str(i) + ")")
			i += 1
	def discoverCertificates(self):
		i = 0
		for line in self.content:
			search = re.search(self.regex_cert, line)
			if search:
				self.sensitive_info.append("Possible Certificate detected at file " + self.name +  " (line " + str(i) + ")")
			i +=1
	def discoverTokens(self):
		i = 0
		for line in self.content:
			for regex in self.regex_token:
				search = re.search(regex, line)					
				if search:
					self.sensitive_info.append("Possible token detected: " +search.group(0)[0:8] + "... at file " + self.name +  " (line " + str(i) + ")")
			i +=1





