from django import forms
from .models import IceCream


class TodoForm(forms.Form):
    description = forms.CharField(max_length=100)
    
    
class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = '__all__'