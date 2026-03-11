from django import forms

class CrearCursoForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True, label="Nombre del Curso")
    descripcion = forms.CharField(widget=forms.Textarea, required=True, min_length=10)

    # Ejemplo de validación personalizada extra
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if "prohibido" in nombre.lower():
            raise forms.ValidationError("Este nombre no está permitido.")
        return nombre
