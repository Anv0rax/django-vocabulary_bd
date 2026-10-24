from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.contrib import messages
from django.utils.translation import gettext as _
from .models import *
from .forms import *
  
# Create your views here.
class IndexView(View) :
    def get(self, request) :
        # messages.success(request, "Profile updated successfully!")
        # messages.error(request, "Profile updated successfully!")
        
        # return render(request, "vocabulary_db/index.html")
        return redirect("words")
    
class ConfirmDelete(View) :
    model = None
    list_name = None
    message = ""

    def get(self, request, pk) :
        obj = get_object_or_404(self.model, pk=pk)
        context = {
            "object" : obj,
            "cancel_url" : self.list_name,
        }
        return render(request, "vocabulary_db/confirm_delete.html", context)

    def post(self, request, pk) :
        obj = get_object_or_404(self.model, pk=pk)
        obj.delete()
        messages.success(request, self.message)
        return redirect(self.list_name)

# =====================================
#               WORDS
# =====================================

class WordsList(View) :
    def get(self, request) :
        words = Word.objects.all()

        context = {
            "bool_navbar" : True,
            "words" : words,
            "active" : "words",
        }

        return render(request, "vocabulary_db/words.html", context)

# class MyFormView(View): # https://docs.djangoproject.com/en/6.1/topics/class-based-views/intro/
#     form_class = MyForm
#     initial = {"key": "value"}
#     template_name = "form_template.html"

#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {"form": form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             # <process form cleaned data>
#             return HttpResponseRedirect("/success/")

#         return render(request, self.template_name, {"form": form})

class AddWord(View) : 
    # https://youtu.be/EX6Tt-ZW0so
    class_form = WordForm

    def get(self, request) :
        context = {
            "form" : self.class_form(),
            "cancel_url" : "words"
        }
        return render(request, "vocabulary_db/crud_form.html", context)

    def post(self, request) :
        form = self.class_form(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, _("Le mot est bien ajouté à la liste !"))
            return redirect("words")
        else : 
            messages.error(request, _("Formulaire non valide !"))
            return redirect("add_word")

class EditWord(View) : 
    class_form = WordForm

    def get(self, request, pk) :
        word = get_object_or_404(Word, word=pk)
        context = {
            "form" : self.class_form(instance=word),
            "edition" : True,
            "cancel_url" : "words",
            "edit_url" : "edit_word",
            "delete_url" : "delete_word",
        }
        return render(request, "vocabulary_db/crud_form.html", context)

    def post(self, request, pk) :
        word = get_object_or_404(Word, word=pk)
        form = self.class_form(request.POST, instance=word)
        if form.is_valid() :
            form.save()
            messages.success(request, _("Le mot est mis à jour !"))
            return redirect("words")
        else : 
            messages.error(request, _("Mise à jour invalide !"))
            return redirect("edit_word", pk=pk)

class DeleteWord(ConfirmDelete) :
    model = Word
    list_name = "words"
    message = _("Le mot est supprimé !")

# =====================================
#               SOURCES
# =====================================

class SourcesList(View) :
    def get(self, request) :
        context = {
            "bool_navbar" : True,
            "title" : _("Liste des sources"),
            "items" : Source.objects.all(),
            "add_url" : "add_source",
            "edit_url" : "edit_source",
            "delete_url" : "delete_source",
            "active" : "sources",
            "sourced" : True,
        }
        return render(request, "vocabulary_db/list_simple.html", context)

class SourceInfo(View) : 
    def get(self, request, pk) :
        source = get_object_or_404(Source, pk=pk)
        context = {
            "bool_navbar" : True,
            "source" : source,
            "words" : source.words.all(),
            "active" : "sources",
        }
        return render(request, "vocabulary_db/source_info.html", context)

class AddSource(View) : 
    class_form = SourceForm

    def get(self, request) :
        context = {
            "form" : self.class_form(),
            "cancel_url" : "sources"
        }
        return render(request, "vocabulary_db/crud_form.html", context)

    def post(self, request) :
        form = self.class_form(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, _("La source est bien ajouté à la liste !"))
            return redirect("sources")
        else : 
            messages.error(request, _("Formulaire non valide !"))
            return redirect("add_source")

class EditSource(View) :
    class_form = SourceForm

    def get(self, request, pk) :
        source = get_object_or_404(Source, pk=pk)
        context = {
            "form" : self.class_form(instance=source),
            "edition" : True,
            "cancel_url" : "sources",
            "delete_url" : "delete_source",
        }
        return render(request, "vocabulary_db/crud_form.html", context)

    def post(self, request, pk) :
        source = get_object_or_404(Source, pk=pk)
        form = self.class_form(request.POST, instance=source)
        if form.is_valid() :
            form.save()
            messages.success(request, _("La source est mise à jour !"))
            return redirect("sources")
        else :
            messages.error(request, _("Mise à jour invalide !"))
            return redirect("edit_source", pk=pk)

class DeleteSource(ConfirmDelete) :
    model = Source
    list_name = "sources"
    message = _("La source est supprimée !")

# =====================================
#               AUTHORS
# =====================================

class AuthorsList(View) :
    def get(self, request) :
        context = {
            "bool_navbar" : True,
            "title" : _("Liste des auteur•ice•s"),
            "items" : Author.objects.all(),
            "add_url" : "add_author",
            "edit_url" : "edit_author",
            "delete_url" : "delete_author",
            "active" : "authors",
        }
        return render(request, "vocabulary_db/list_simple.html", context)

class AddAuthor(View) :
    class_form = AuthorForm

    def get(self, request) :
        context = {
            "form" : self.class_form(),
            "cancel_url" : "authors",
        }
        return render(request, "vocabulary_db/crud_form.html", context)

    def post(self, request) :
        form = self.class_form(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, _("L'auteur•ice est bien ajouté•e à la liste !"))
            return redirect("authors")
        else :
            messages.error(request, _("Formulaire non valide !"))
            return redirect("add_author")

class EditAuthor(View) :
    class_form = AuthorForm

    def get(self, request, pk) :
        author = get_object_or_404(Author, pk=pk)
        context = {
            "form" : self.class_form(instance=author),
            "edition" : True,
            "cancel_url" : "authors",
            "delete_url" : "delete_author",
        }
        return render(request, "vocabulary_db/crud_form.html", context)

    def post(self, request, pk) :
        author = get_object_or_404(Author, pk=pk)
        form = self.class_form(request.POST, instance=author)
        if form.is_valid() :
            form.save()
            messages.success(request, _("L'auteur•ice est mis•e à jour !"))
            return redirect("authors")
        else :
            messages.error(request, _("Mise à jour invalide !"))
            return redirect("edit_author", pk=pk)

class DeleteAuthor(ConfirmDelete) :
    model = Author
    list_name = "authors"
    message = _("L'auteur•ice est supprimé•e !")

# =====================================
#               TYPES
# =====================================

class TypesList(View) :
    def get(self, request) :
        context = {
            "bool_navbar" : True,
            "title" : _("Liste des types"),
            "items" : TypeSource.objects.all(),
            "add_url" : "add_type",
            "edit_url" : "edit_type",
            "delete_url" : "delete_type",
            "active" : "types",
        }
        return render(request, "vocabulary_db/list_simple.html", context)

class AddType(View) :
    class_form = TypeSourceForm

    def get(self, request) :
        context = {
            "form" : self.class_form(),
            "cancel_url" : "add_source",
        }
        return render(request, "vocabulary_db/crud_form.html", context)

    def post(self, request) :
        form = self.class_form(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, _("Le type est bien ajouté à la liste !"))
            return redirect("add_source")
        else :
            messages.error(request, _("Formulaire non valide !"))
            return redirect("add_type")

class EditType(View) :
    class_form = TypeSourceForm

    def get(self, request, pk) :
        type_source = get_object_or_404(TypeSource, pk=pk)
        context = {
            "form" : self.class_form(instance=type_source),
            "edition" : True,
            "cancel_url" : "types",
            "delete_url" : "delete_type",
        }
        return render(request, "vocabulary_db/crud_form.html", context)

    def post(self, request, pk) :
        type_source = get_object_or_404(TypeSource, pk=pk)
        form = self.class_form(request.POST, instance=type_source)
        if form.is_valid() :
            form.save()
            messages.success(request, _("Le type est mis à jour !"))
            return redirect("types")
        else :
            messages.error(request, _("Mise à jour invalide !"))
            return redirect("edit_type", pk=pk)

class DeleteType(ConfirmDelete) :
    model = TypeSource
    list_name = "types"
    message = _("Le type est supprimé !")