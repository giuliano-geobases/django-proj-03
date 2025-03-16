from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#def home(request):
#    return HttpResponse('*** HOME - 01 ***')

def home(request):
    return render(request, 'home.html', context={
        'name': 'GG Gataun!!!',
    })
