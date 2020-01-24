from django import forms
from .models import Fashion

class FashionForm(forms.ModelForm):

    class Meta:
        model = Fashion
        fields = ('user', 'message','image' )
        