from django.forms import ModelForm
from django import forms

from django.utils.translation import gettext as _

from .models import *

class BaseNewFormInput :
    template_name = "vocabulary_db/widget-form-options.html"

    def __init__(self, *args, add_url=None, add_label=None, **kwargs):
        self.add_url = add_url
        self.add_label = add_label
        super().__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["add_url"] = self.add_url
        context["widget"]["add_label"] = self.add_label
        return context

class NewCheckBoxAdd(BaseNewFormInput, forms.CheckboxSelectMultiple) : pass
class NewRadioBoxAdd(BaseNewFormInput, forms.RadioSelect) : pass

# https://stackoverflow.com/questions/28764571/display-image-from-imagefield-by-means-of-form

from django.utils.html import format_html

class PictureWidget(forms.widgets.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        if value and hasattr(value, 'url'):
            preview = format_html(
                '<img src="{}" class="img-fluid rounded mb-2 d-block preview_image_form" />',
                value.url
            )
            return preview + html
        return html

class WordForm(ModelForm) :
    class Meta :
        model = Word
        fields = ["sources", "word", "translation", "explainations_fr", "explainations_en", "mastered", "added"] # "__all__" 
        widgets = {
            "sources" : NewCheckBoxAdd(
                add_label=_("Ajouter une source"),
                add_url="add_source",
                attrs={"class": "form-check-input"}),
            "word" : forms.TextInput(attrs={"class" : "form-control"}),
            "translation" : forms.TextInput(attrs={"class" : "form-control"}),
            "explainations_fr" : forms.Textarea(attrs={"class" : "form-control", "rows" :"3"}),
            "explainations_en" : forms.Textarea(attrs={"class" : "form-control", "rows" :"3"}),
            "mastered" : forms.CheckboxInput(attrs={"class" : "form-check-input"}),
            "added": forms.DateInput(attrs={"class" : "form-control", "type" : "date"}),
        }

class SourceForm(ModelForm) :
    class Meta :
        model = Source
        fields = ["type", "title_fr", "title_en", "author", "release_date", "image"] # "__all__" 
        widgets = {
            "type" : NewRadioBoxAdd(
                add_label=_("Ajouter un type"),
                add_url="add_type",
                attrs={"class": "form-check-input"}),
            'title_fr' : forms.TextInput(attrs={'class' : 'form-control'}),
            'title_en' : forms.TextInput(attrs={'class' : 'form-control'}),
            "author" : NewRadioBoxAdd(
                add_label=_("Ajouter un•e auteur•ice"),
                add_url="add_author",
                attrs={"class": "form-check-input"}),
            "release_date": forms.DateInput(attrs={"class" : "form-control", "type" : "date"}),
            "image" : PictureWidget(attrs={"class" : "form-control", "type" : "file"})
        }

class AuthorForm(ModelForm) :
    class Meta :
        model = Author
        fields = ["name",]
        widgets = {
            "name" : forms.TextInput(attrs={"class" : "form-control"}),
        }

class TypeSourceForm(ModelForm) :
    class Meta :
        model = TypeSource
        fields = ["type_fr", "type_en",]
        widgets = {
            "type_fr" : forms.TextInput(attrs={"class" : "form-control"}),
            "type_en" : forms.TextInput(attrs={"class" : "form-control"}),
        }