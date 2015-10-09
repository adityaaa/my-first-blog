from django.db import models
from datetime import datetime
from django.utils import timezone
from time import time

# Create your models here.
def get_upload_file_name(instance,filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

class Article(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	likes = models.IntegerField(default=0)
	author = models.CharField(max_length = 50,default = '')
	category = models.CharField(max_length = 100, default = '')
	pub_date = models.DateTimeField('date published')
	hero_image = models.FileField(upload_to=get_upload_file_name,default='')


	def __str__(self):
		return self.title	
	