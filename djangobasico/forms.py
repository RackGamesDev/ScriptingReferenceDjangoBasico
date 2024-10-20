from django import forms
#from django.forms import ModelForm #para combinar modelos y forms, por que se parecen mucho
#from ..datos.models import Usuario


class ComentarioForm(forms.Form): #al crear formularios de esta manera es muy parecido a como se crean modelos en models.py
    nombre = forms.CharField(label="Escribe nombre", max_length=100, help_text="100 maximo") #creando cada input, dependiendo del tipo se validan de cada manera y tienen propiedades
    url = forms.URLField(label="una pagina", required=False)
    numero = forms.IntegerField(required=False, max_value=100, initial=3)
    correo = forms.EmailField(label="Correo", required=False, 
        widget=forms.EmailInput(attrs={'class': 'inputClase'})) #con widget se pueden poner atributos para css (aqui se le especifica una clase) (bastante combinable con bootstrap)

    def clean_nombre(self): #para hacer validaciones extra sobre un campo
        nombre = self.cleaned_data.get("nombre")
        if nombre == "hola":
            raise forms.ValidationError("no puede ser hola") #en caso de no ser valido
        else:
            return nombre #en caso de ser valido

#class UsuarioForm(ModelForm): #creando el form a partir del model
#    class Meta:
#        model = Usuario
#        fields = ['nombre', 'dinero'] #campos a usar, tambien se podria usar = '__all__'
#        extra_fields = ['permiso']