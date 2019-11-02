from .models import Business
from django import forms
        
class BusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    fields = ['image','name','use','email','hoods'] 
    