from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(
        '''<h1>Nada por aqui</h1>
           <h2>Se estiver procurando pela API, acesse a url: /api/v1</h2>'''
    )