from django import forms
from .models import Signup,Patient

class SignupForm(forms.ModelForm):
    class Meta:
        model=Signup
        fields='__all__'

class PatientForm(forms.ModelForm):
    class Meta:
        model= Patient
        fields='__all__'       