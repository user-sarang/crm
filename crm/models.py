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
		return self.name

	class Meta:
		unique_together = ["name", "email", "phone_number"]	

class Campaign(models.Model):
	name = models.CharField(max_length=200)
	data_added = models.DateTimeField(blank=True, null=True)

	def save_campaign(self):
		self.data_added = timezone.now()
		self.save()

	def __str__(self):
		return self.name


class Campaign_enrollment(models.Model):
	lead = models.ForeignKey('crm.Lead')
	Campaign = models.ForeignKey('crm.Campaign')
	data_added = models.DateTimeField(blank=True, null=True)

	def save_campaign_enrollment(self):
		self.data_added = timezone.now()
		self.save()

	def __str__(self):
		return self.Campaign.name

class Document(models.Model):
	docfile = models.FileField(upload_to='%Y/%m/%d')
	
