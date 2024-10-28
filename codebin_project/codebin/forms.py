from django    import forms

from .models import Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'code', 'language']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'code':forms.Textarea(attrs={'class':'form-control'}),
            'language':forms.TextInput(attrs={'class':'form-control'}),}
        
    