from django.db import models
from django.db.models.signals import pre_save, post_save


class File(models.Model):
	upload = models.FileField(upload_to='files')

	location = models.CharField(max_length=500, null=True)
	file_type = models.CharField(max_length=100, null=True)
	size = models.IntegerField(null=True)
	upload_datetime = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.upload.name


def pre_save_file_info(sender, instance, *args,**kwargs):
	instance.location = instance.upload.url
	instance.size = instance.upload.size

pre_save.connect(pre_save_file_info, sender=File)