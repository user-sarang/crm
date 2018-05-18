from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Campaign, Document, Lead, Campaign_enrollment, Comment
from django.http import HttpResponseRedirect, HttpResponse
from .forms import DocumentForm
from .lead_importer import read_csv
from django.http import JsonResponse
from django.core import serializers
from django.utils import timezone

# Create your views here.
def campaign_list(request):
	campaigns = Campaign.objects.all()
	print(campaigns)
	return render(request, 'crm/campaign_list.html',{'campaigns': campaigns})


def campaign_detail(request, pk):
	#get current campaign
	campaign = get_object_or_404(Campaign, pk=pk)

	#If file upload was selected
	if request.method == 'POST':
		# Create a new document model form
		form = DocumentForm(request.POST, request.FILES)
		
		# Check if form is valid
		if form.is_valid():
			#Create a new document model object
			file = Document(docfile=request.FILES['docfile'])

			#Saving uploaded file to database
			file.save()

			#Process the file
			lead_data, errors = read_csv(file.docfile.path)

			# If lead data is none, we need to show why there are errors
			if lead_data is None:
				return render(request, 'crm/invalid_file.html',{'errors':errors})

			# If lead data is present, we will save it in the DB
			unique_leads = 0;
			for lead in lead_data:
				lead_entry, creation_status =Lead.objects.get_or_create(	name = lead["full_name"],
									email = lead["email"], 
									phone_number = lead["phone_number"])

				# Storing if lead already exists or not.
				lead['creation_status'] = creation_status
				if creation_status is True:
					unique_leads = unique_leads+1
					
					# Adding lead to the respective campaign
					Campaign_enrollment.objects.create(lead = lead_entry, Campaign=campaign)
				

				# Saving entry to database
				lead_entry.save()

			# Create users if not exists
			return render(request, 'crm/file_upload.html',
				{	'campaign': campaign,
					'file':file,
					'lead_data': lead_data,
					'unique_leads':unique_leads
				})
			#return HttpResponseRedirect(reverse('campaign_detail',args=pk))
	else:
		form = DocumentForm()  # A empty, unbound form
	
	# Load documents for the list page
	documents = Document.objects.all()	
	enrollments = Campaign_enrollment.objects.filter(Campaign = campaign)
	return render(request, 'crm/campaign_detail.html', {'campaign': campaign,'enrollments': enrollments})

def campaign_enrollment_details(request, campaign_id, lead_id):

	campaign_data = Campaign.objects.get(pk=campaign_id)
	lead_data = Lead.objects.get(pk=lead_id)
	ce = Campaign_enrollment.objects.filter(Campaign= campaign_data, lead=lead_data)



	if request.method == "GET":
		
		comments = Comment.objects.filter(campaign_enrollment=ce[0])
		
		data = []

		data.append(lead_data)

		for comment in comments: data.append(comment)

		
		data = serializers.serialize("json", data)
		return HttpResponse(data, content_type='json')


	if request.method == "POST":
		print ("##################")
		ce[0].modify_campaign_enrollment()
		comment = Comment(campaign_enrollment = ce[0], text=request.POST.get('comment_data'))
		comment.save_comment()

		if lead_data.date_modified is None:
			lead_data.modify_lead()
			
		if comment.date_added > lead_data.date_modified: lead_data.modify_lead()


		return HttpResponse('<h1>Success!</h1   >')




def delete_file(request, pk):
	try:
		file = Document.objects.get(pk=pk)
		file.delete()
	except Document.DoesNotExist:
		file=None
	return render(request, 'crm/deleted_file.html',{'file':file})

