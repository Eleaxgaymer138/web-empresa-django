from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder':'Aqui escribe tu Nombre'}
        ))
    email = forms.EmailField(label="E-mail",required=True, widget=forms.EmailInput(
        attrs={"class": "form-control", 'placeholder':'Aqui escribe tu E-mail'}
        ))
    content = forms.CharField(label="Contenido",required=True, widget=forms.Textarea(
        attrs={"class": "form-control", 'rows': 3, 'placeholder':'Aqui escribe tu mensaje'}
        ))