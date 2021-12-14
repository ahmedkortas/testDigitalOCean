from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# take a request and return a response
#the request will fetch all the data from the database in the table visits
#the response will be a list of all the data in the table visits
def vistis_view(request):
    return HttpResponse("Hello, world. You're at the visits index.")