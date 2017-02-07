from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from shortuuidfield import ShortUUIDField
from PIL import Image

# Create your models here.

class Post(models.Model):
	uuid = ShortUUIDField(unique=True)
	title = models.CharField(max_length=128)
	owner = models.ForeignKey(User)
	image = models.ImageField(null=True, blank=True)
	created_on = models.DateField(auto_now_add=True)

	class Meta:
		#verbose_name_plural = 'posts'
		ordering = ['-created_on']
	
	def __unicode__(self):
		return u"%s" %self.title

	def __str__(self):
		return self.title

	@models.permalink
	# this method will return the URL address to the model instance referenced
	def get_absolute_url(self):
		return 'post_detail', [self.uuid]

	# def get_update_url(self):
	# 	return 'post_update', [self.uuid]


