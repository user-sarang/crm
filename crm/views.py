from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Campaign, Document
from django.http import HttpResponseRedirect
from .forms import DocumentForm
from .custom_csv_reader import read_csv

# Create your views here.
def campaign_list(request):
	campaigns = Campaign.objects.all()
	print(campaigns)
	return render(request, 'crm/campaign_list.html',{'campaigns': campaigns})


def campaign_detail(request, pk):
	campaign = get_object_or_404(Campaign, pk=pk)
	if request.method == 'POST':
		print('heere.....')
		form = DocumentForm(request.POST, request.FILES)
		print(form.errors)
		if form.is_valid():
			file = Document(docfile=request.FILES['docfile'])
			file.save()
			read_csv(file.docfile.path)
			return render(request, 'crm/file_upload.html',{'campaign': campaign,'file':file})
			#return HttpResponseRedirect(reverse('campaign_detail',args=pk))
	else:
		form = DocumentForm()  # A empty, unbound form
	
	# Load documents for the list page
	documents = Document.objects.all()	
	return render(request, 'crm/campaign_detail.html', {'campaign': campaign,'documents':documents})

def delete_file(request, pk):
	try:
		file = Document.objects.get(pk=pk)
		file.delete()
	except Document.DoesNotExist:
		file=None
	return render(request, 'crm/deleted_file.html',{'file':file})

