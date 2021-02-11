from django.shortcuts import render
# from django.http import HttpResponse

from .form import UserForm, UserFormM

# Create your views here.

def usuarios(request):
    data = {}
    if request.method == 'POST':
        filled_form = UserFormM(request.POST)
        if filled_form.is_valid():
            user = filled_form.save()
            data = {'user': user}
    return render(request, 'usuarios.html', data)

def add_usuarios1(request):
    return render(request, 'add_usuarios1.html')

def add_usuarios2(request):
    data = {'form': UserForm()}
    return render(request, 'add_usuarios2.html', data)

def add_usuarios3(request):
    data = {'form': UserFormM()}
    return render(request, 'add_usuarios3.html', data)
