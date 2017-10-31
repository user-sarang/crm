from django.shortcuts import render

# Create your views here.
def campaign_list(request):
	return render(request, 'crm/campaign_list.html')
