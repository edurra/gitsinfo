from django.db import models

# Create your models here.

class Repository(models.Model):
	name = models.CharField(max_length=300)
	periodicscan = models.BooleanField(default = True)
	def __str__(self):
		return self.name

class Finding(models.Model):
	repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
	finding = models.CharField(max_length = 400)
	date = models.DateTimeField('Date of finding')
	solved = models.BooleanField(default = False)
	def __str__(self):
		return self.finding
