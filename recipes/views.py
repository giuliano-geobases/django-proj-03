from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#def home(request):
#    return HttpResponse('*** HOME - 01 ***')

def home(request):
    return render(request, 'home.html', context={
        'name': 'GG Gataun!!!',
    })

def contact(request):
    return HttpResponse('*** CONTATO - 27-99999.3344 ***')

def about(request):
    return HttpResponse('*** SOBRE NÓS ==>> EU  E TU ***')