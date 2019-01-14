from django.db import models

class Paste(models.Model):
	text = models.TextField()
	name = models.CharField(max_length = 40, null = True, blank = True)
	created_on = models.DateTimeField(auto_now_add = True)
	updated_on = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return self.name or str(self.id)
		


		
