from django.db import models
from django.utils import timezone

# Create your models here.
class Lead(models.Model):
	name = models.CharField(max_length=200)
	data_added = models.DateTimeField(blank=True, null=True)
	email = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=20)

	def save_lead(self):
		self.data_added = timezone.now()
		self.save()

	def __str__(self):
		return self.title



class Campaign(models.Model):
	name = models.CharField(max_length=200)
	data_added = models.DateTimeField(blank=True, null=True)
	lead = models.ForeignKey('crm.Lead')

	def create(self):
		self.data_added=timezone.now()

	def __str__(self):
		return self.title
