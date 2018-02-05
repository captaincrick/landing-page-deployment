from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ('name','email','phone_number',)
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'Full Name'}),
            'email':forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'Email'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'Phone Number'})
            }
