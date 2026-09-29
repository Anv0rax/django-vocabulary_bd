from django.forms import ModelForm
from django import forms
from .models import *

class BaseNewFormInput :
    template_name = 'vocabulary_db/widget-form-options.html'

    def __init__(self, *args, add_url=None, add_label=None, **kwargs):
        self.add_url = add_url
        self.add_label = add_label
        super().__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['add_url'] = self.add_url
        context['widget']['add_label'] = self.add_label
        return context

class NewCheckBoxAdd(BaseNewFormInput, forms.CheckboxSelectMultiple) : pass
class NewRadioBoxAdd(BaseNewFormInput, forms.RadioSelect) : pass

class WordForm(ModelForm) :
    class Meta :
        model = Word
        fields = ['sources', 'word', 'translation', 'explainations', 'mastered', 'added'] # '__all__' 
        widgets = {
            'sources' : NewCheckBoxAdd(
                add_label='Ajouter une source',
                add_url='add_source',
                attrs={'class': 'form-check-input'}),
            'word' : forms.TextInput(attrs={'class' : 'form-control'}),
            'translation' : forms.TextInput(attrs={'class' : 'form-control'}),
            'explainations' : forms.Textarea(attrs={'class' : 'form-control', 'rows' :'3'}),
            'mastered' : forms.CheckboxInput(attrs={'class' : 'form-check-input'}),
            'added': forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'}),
        }

class SourceForm(ModelForm) :
    class Meta :
        model = Source
        fields = ['type', 'title', 'author', 'release_date',] # '__all__' 
        widgets = {
            'type' : NewRadioBoxAdd(
                add_label='Ajouter un type',
                add_url='add_type',
                attrs={'class': 'form-check-input'}),
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'author' : NewRadioBoxAdd(
                add_label='Ajouter un•e auteur•ice',
                add_url='add_author',
                attrs={'class': 'form-check-input'}),
            'release_date': forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'}),
        }

class AuthorForm(ModelForm) :
    class Meta :
        model = Author
        fields = ['name',]
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

class TypeSourceForm(ModelForm) :
    class Meta :
        model = TypeSource
        fields = ['type',]
        widgets = {
            'type' : forms.TextInput(attrs={'class' : 'form-control'}),
        }