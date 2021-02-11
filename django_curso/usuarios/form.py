from django import forms
from .models import Usuario

class UserForm(forms.Form):
    GENEROS = [('M','Hombre'),('F','Mujer'),('O','Otros')]

    username =  forms.CharField(label='Nombre de usuario', max_length=100)
    email = forms.EmailField(label='Correo', max_length=50)
    gender = forms.ChoiceField(label='Genero', choices=GENEROS)

    passw = forms.CharField(label='Contraleña', max_length=20, 
            widget=forms.PasswordInput)
    comentarios =  forms.CharField(label='Comentarios', max_length=400,
            widget=forms.Textarea)
    gender2 = forms.MultipleChoiceField(label='Genero', choices=GENEROS,
        widget=forms.CheckboxSelectMultiple) 
    gender3 = forms.ChoiceField(label='Genero', choices=GENEROS,
        widget=forms.RadioSelect)

class UserFormM(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'gender']
        labels = {
            'username': 'Nombre de usuario', 
            'email': 'Correo', 
            'gender': 'Género'
        }  