# https://dev.to/doridoro/django-translation-translate-database-content-26ei

from modeltranslation.translator import register, TranslationOptions
from .models import Source, TypeSource, Word

@register(Source)
class SourceTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(TypeSource)
class TypeSourceTranslationOptions(TranslationOptions):
    fields = ('type',)

@register(Word)
class TypeSourceTranslationOptions(TranslationOptions):
    fields = ('explainations',)