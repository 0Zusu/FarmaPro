from django import forms

class formulario(forms.Form):
    NombrePaciente = forms.CharField(max_length=50, label="Nombre del Paciente",required=True, widget=forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Ingrese Nombre del Paciente'}))
    RutPaciente = forms.CharField(max_length=20, label="Rut Paciente",required=True,widget=forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Ingrese Rut del Paciente'}))
    NombreMedicamento = forms.CharField(max_length=50, label="Nombre del Medicamento",required=True, widget=forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Ingrese Nombre del Medicamento'}))
    Dosis = forms.IntegerField(label="Dosis del medicamento en gramos",required=True, widget=forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Ingrese dosis del medicamento'}))
    Motivo = forms.CharField(label="Motivo Prescripcion",required=True,widget=forms.Textarea(attrs={'class':'form-control mb-3','placeholder':'Ingrese Motivo'}))
    Firma = forms.ImageField(label="Archivo Firma Electronica",required=False)