from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html, format_html_join
from django.utils.safestring import mark_safe

from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext, gettext_lazy as _

from .models import *



# Info de connexion dans private.py 

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin) :
    list_display = ["name", "view_sources_link"]
    ordering = ["id"]
    # readonly_fields = [""]
    search_fields = ["id", "name"]
    readonly_fields = ["source_list",]

    def view_sources_link(self, obj):
        url = (
            reverse("admin:vocabulary_db_source_changelist")
            + f"?author__id__exact={obj.id}"
        )
        return format_html('<a href="{}">{}</a>', url, _("Voir les sources"))
    view_sources_link.short_description = _("Sources associées")


    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields
        return []

    def source_list(self, obj):
        if not obj.pk:
            return "-"
        
        sources = obj.sources.all()
        if not sources:
            product_links = _("Aucune source associée")
        else:
            product_links = format_html_join(
                mark_safe("<br>"), '<a href="{}">{}</a>', (
                    (reverse("admin:vocabulary_db_source_change", args=[s.pk]), s, )
                    for s in sources
                ))

        add_url = (
            reverse("admin:vocabulary_db_source_add")
            + f"?author={obj.pk}"
        )
        add_link = format_html(
            '<br><br><a class="addlink" href="{}">{}</a>',
            add_url, _("Ajouter une source")
        )
        return format_html("{}{}", product_links, add_link)
    source_list.short_description = _("Sources associées")




@admin.register(TypeSource)
class TypeSourceAdmin(TranslationAdmin) :
    list_display = ["type",] 
    ordering = ["id"]
    # readonly_fields = [""]
    search_fields = ["id", "type"]






@admin.register(Source)
class SourceAdmin(TranslationAdmin) :
    list_display = ["source_with_image", "id", "type", "author", "release_date", "view_words_link"]
    ordering = ["release_date", "title", "id"]
    # readonly_fields = [""]
    search_fields = ["id", "title"]
    readonly_fields = ["image_preview","word_list",]
    list_filter = ["author"]

    def source_with_image(self, obj):
        if obj.image:
            return format_html(
                '<div style="display:flex; align-items:center;">'
                '<img src="{}" style="max-width:32px; margin-right:6px;" />'
                '{}'
                '</div>',
                obj.image.url, obj.title,
            )
        return obj.title
    source_with_image.short_description = _("Titre")
    source_with_image.admin_order_field = "title"

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:200px" />', obj.image.url)
        return _("Pas d'image")
    image_preview.short_description = _("Prévisualisation")

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields
        return []

    def word_list(self, obj):
        if not obj.pk:
            return "-"
        
        words = obj.words.all()
        if not words:
            product_links = _("Aucun mot associé")
        else:
            product_links = format_html_join(
                mark_safe("<br>"), '<a href="{}">{}</a>', (
                    (reverse("admin:vocabulary_db_word_change", args=[w.word]), w.word, )
                    for w in words
                ))

        add_url = (
            reverse("admin:vocabulary_db_word_add")
            + f"?source={obj.pk}"
        )
        add_link = format_html(
            '<br><br><a class="addlink" href="{}">{}</a>',
            add_url, _("Ajouter un mot")
        )

        return format_html("{}{}", product_links, add_link)

    word_list.short_description = _("Mots associés")

    def view_words_link(self, obj):
        url = (
            reverse("admin:vocabulary_db_word_changelist")
            + f"?sources__id__exact={obj.id}"
        )
        return format_html('<a href="{}">{}</a>', url, _("Voir les mots"))
    view_words_link.short_description = _("Mots associés")







@admin.register(Word)
class WordAdmin(TranslationAdmin) :
    list_display = ["word", "translation", "explainations", "mastered", "added"] # "__all__" 
    ordering = ["word"]
    # readonly_fields = [""]
    search_fields = ["word", "translation"]
    list_filter = ["sources"]

