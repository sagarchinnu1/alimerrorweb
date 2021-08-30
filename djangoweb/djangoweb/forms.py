from django import forms 
from django.contrib import messages

class StudentForm(forms.Form):    
    file      = forms.FileField(help_text="Please upload the correct import error file with .xlsx extension")
    #messages.add_message(level=1,message="import error File")
    file2     = forms.FileField(help_text="Please upload the correct load sheet file of import error with .xlsx extension") 
    #messages.add_message(level=2,message="load sheet of import error")