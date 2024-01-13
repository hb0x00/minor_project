from django import forms
from Project.models import SeekerDetail

class DocumentForm(forms.ModelForm):
    class Meta:
        model = SeekerDetail
        fields = "__all__"
