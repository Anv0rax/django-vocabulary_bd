from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Author(models.Model) :
    name = models.CharField(max_length=50, verbose_name=_("Nom"))

    class Meta : 
        ordering = ('name', )
        verbose_name = _("Auteur•rice")
        verbose_name_plural = _("Auteur•rice•s")

    def __str__(self) :
        return self.name

class TypeSource(models.Model) :
    type = models.CharField(max_length=50, verbose_name=_("Type"))

    class Meta : 
        ordering = ('type', )
        verbose_name = _("Type")
        verbose_name_plural = _("Types")

    def __str__(self) :
        return self.type

class Source(models.Model) :
    title = models.CharField(max_length=50, verbose_name=_("Titre"))
    release_date = models.DateField(verbose_name=_("Date de sortie"))
    type = models.ForeignKey(TypeSource, verbose_name=_("Type de source"), related_name="sources", on_delete=models.SET_NULL, null=True)
    # https://stackoverflow.com/questions/2642613/what-is-related-name-used-for
    author = models.ForeignKey(Author, verbose_name=_("Auteur"), related_name="sources", on_delete=models.SET_NULL, null=True)
    # https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
    # https://stackoverflow.com/questions/8609192/what-is-the-difference-between-null-true-and-blank-true-in-django
    image = models.ImageField(default="", upload_to="", verbose_name=_("Image"), blank=True, null=True)

    class Meta : 
        ordering = ('release_date', 'title', 'id', )
        verbose_name = _("Source")
        verbose_name_plural = _("Sources")

    def __str__(self) :
        if self.author is None :
            return self.title
        return f'{self.author.name} - {self.title}'

class Word(models.Model) :
    word = models.CharField(primary_key=True, max_length=50, verbose_name=_("Mot"))
    translation = models.CharField(max_length=50, verbose_name=_("Traduction"))
    explainations = models.CharField(max_length=500, verbose_name=_("Explications"), blank=True, null=True)
    mastered = models.BooleanField(verbose_name=_("Maîtrisé"), default=False)
    added = models.DateTimeField(verbose_name=_("Ajouté le"), default=timezone.now, blank=True)
    sources = models.ManyToManyField(Source, verbose_name=_("Sources"), related_name="words", blank=True)
    # https://stackoverflow.com/questions/61566808/manytomany-relationship-between-two-models-in-django

    class Meta :
        ordering = ('mastered', '-added', 'word', )
        verbose_name = _("Mot")
        verbose_name_plural = _("Mots")

    def __str__(self) :
        return f"{self.word} = {self.translation}"