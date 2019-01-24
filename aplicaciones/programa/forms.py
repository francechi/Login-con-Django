from aplicaciones.programa.models import Programa
from django import forms

class ProgramaForm(forms.ModelForm):
    
    class Meta:
        model = Programa

        fields = [
            'nombre',
            'tipo',
            'version',
            'fecha',
            'persona',
            'extensiones',
        ]
        labels = {#Etiquetas
            'nombre': 'Nombre',
            'tipo': 'Tipo',
            'version': 'Versión',
            'fecha': 'Fecha',
            'persona': 'Persona',
            'extensiones': 'Extensiones',
        }
        widgets ={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
            'version': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.TextInput(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
            'extensiones': forms.CheckboxSelectMultiple()
        }