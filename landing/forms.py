from django import forms

from landing.models import DictionaryTerm


class DictionaryTermAdminForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = DictionaryTerm
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }


