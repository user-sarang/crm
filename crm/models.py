from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Lead(models.Model):
	name = models.CharField(max_length=200)
	data_added = models.DateTimeField(blank=True, null=True)
	email = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=20)
	date_modified = models.DateTimeField(blank=True, null=True, default=datetime.datetime(year=1999,day=1, month=1))

	def save_lead(self):
		self.data_added = timezone.now()
		self.save()

	def modify_lead(self):
		self.date_modified = timezone.now()
		self.save()

	def __str__(self):
		return self.name


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
	date_added = models.DateTimeField(blank=True, null=True)
	date_modified= models.DateTimeField(blank=True, null=True)


	def modify_campaign_enrollment(self):
		self.date_modified = timezone.now()
		self.save()

	def save_campaign_enrollment(self):
		self.date_added = timezone.now()
		self.save()

	def __str__(self):
		return self.Campaign.name

class Document(models.Model):
	docfile = models.FileField(upload_to='%Y/%m/%d')
	

class Comment(models.Model):

	campaign_enrollment = models.ForeignKey('crm.Campaign_enrollment')
	date_added = models.DateTimeField(blank=True, null=True)
	text = models.CharField(max_length=100)

	def save_comment(self):
		self.date_added = timezone.now()
		self.save()


	def __str__(self):
		return self.campaign_enrollment.lead.name