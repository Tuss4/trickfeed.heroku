from django.db import models

# The data model for storing favorite videos.
# The username and video id are stored in the database.

class Favorite(models.Model):
	user = models.CharField(max_length=30)
	video = models.CharField(max_length=30)

	def __unicode__(self):
		return self.video

	class Meta:
		ordering = ['-id']