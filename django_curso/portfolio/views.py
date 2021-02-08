from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')
    

def portfolio(request):
    # return HttpResponse('<h1>Portfolio</h1>')
    autor = 'Alejandro Cerezo'
    mail = 'alce65@hotmail.es'
    return render(request,'portfolio.html', {
        'autor' : autor,
        'correo' : mail
    })