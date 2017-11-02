from django.contrib import admin
from .models import Lead, Campaign, Campaign_enrollment, Document
# Register your models here.
admin.site.register(Lead)
admin.site.register(Campaign)
admin.site.register(Campaign_enrollment)
admin.site.register(Document)
