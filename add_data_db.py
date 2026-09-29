# 100% from claude

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sem_04_web_proj.settings')  # adapte le nom
django.setup()

from datetime import datetime
from django.utils import timezone
from vocabulary_db.models import Author, TypeSource, Source, Word  # adapte le nom de l'app

# --- Nettoyage (optionnel, décommente si tu veux repartir de zéro) ---
Word.objects.all().delete()
Source.objects.all().delete()
Author.objects.all().delete()
TypeSource.objects.all().delete()

# --- Types de sources ---
type_livre, _ = TypeSource.objects.get_or_create(type="Livre")
type_serie, _ = TypeSource.objects.get_or_create(type="Série")
type_film, _ = TypeSource.objects.get_or_create(type="Film")
type_podcast, _ = TypeSource.objects.get_or_create(type="Podcast")

# --- Auteurs ---
auteur_rowling, _ = Author.objects.get_or_create(name="J.K. Rowling")
auteur_tolkien, _ = Author.objects.get_or_create(name="J.R.R. Tolkien")
auteur_duffer, _ = Author.objects.get_or_create(name="Duffer Brothers")
auteur_nolan, _ = Author.objects.get_or_create(name="Christopher Nolan")
auteur_inconnu, _ = Author.objects.get_or_create(name="Anonyme")

# --- Sources ---
source_hp, _ = Source.objects.get_or_create(
    title="Harry Potter and the Philosopher's Stone",
    defaults={"release_date": datetime(1997, 6, 26).date(), "type": type_livre, "author": auteur_rowling},
)
source_lotr, _ = Source.objects.get_or_create(
    title="The Lord of the Rings",
    defaults={"release_date": datetime(1954, 7, 29).date(), "type": type_livre, "author": auteur_tolkien},
)
source_strangerthings, _ = Source.objects.get_or_create(
    title="Stranger Things",
    defaults={"release_date": datetime(2016, 7, 15).date(), "type": type_serie, "author": auteur_duffer},
)
source_inception, _ = Source.objects.get_or_create(
    title="Inception",
    defaults={"release_date": datetime(2010, 7, 16).date(), "type": type_film, "author": auteur_nolan},
)
source_podcast, _ = Source.objects.get_or_create(
    title="English Learning for Curious Minds",
    defaults={"release_date": datetime(2020, 3, 10).date(), "type": type_podcast, "author": auteur_inconnu},
)

# --- Mots ---
words_data = [
    {"word": "wizard", "translation": "sorcier", "explainations": "Personne qui pratique la magie.",
     "mastered": True, "added": timezone.make_aware(datetime(2026, 8, 1, 10, 30)), "sources": [source_hp]},
    {"word": "spell", "translation": "sortilège", "explainations": "Peut aussi vouloir dire 'épeler'.",
     "mastered": True, "added": timezone.make_aware(datetime(2026, 8, 2, 14, 15)), "sources": [source_hp]},
    {"word": "cauldron", "translation": "chaudron", "explainations": None,
     "mastered": False, "added": timezone.make_aware(datetime(2026, 8, 5, 9, 0)), "sources": [source_hp]},
    {"word": "ring", "translation": "anneau", "explainations": "Peut aussi signifier 'sonner'.",
     "mastered": True, "added": timezone.make_aware(datetime(2026, 8, 10, 16, 45)), "sources": [source_lotr]},
    {"word": "quest", "translation": "quête", "explainations": None,
     "mastered": False, "added": timezone.make_aware(datetime(2026, 8, 12, 11, 20)), "sources": [source_lotr]},
    {"word": "upside down", "translation": "à l'envers", "explainations": "Désigne aussi la dimension parallèle dans Stranger Things.",
     "mastered": True, "added": timezone.make_aware(datetime(2026, 8, 18, 20, 0)), "sources": [source_strangerthings]},
    {"word": "eerie", "translation": "inquiétant / étrange", "explainations": "Ambiance surnaturelle.",
     "mastered": False, "added": timezone.make_aware(datetime(2026, 8, 20, 19, 30)), "sources": [source_strangerthings]},
    {"word": "dream", "translation": "rêve", "explainations": None,
     "mastered": True, "added": timezone.make_aware(datetime(2026, 8, 25, 8, 10)), "sources": [source_inception]},
    {"word": "maze", "translation": "labyrinthe", "explainations": "Synonyme : 'labyrinth'.",
     "mastered": False, "added": timezone.make_aware(datetime(2026, 9, 1, 13, 0)), "sources": [source_inception]},
    {"word": "fluent", "translation": "courant / fluide", "explainations": "'To be fluent in English' = parler couramment anglais.",
     "mastered": True, "added": timezone.make_aware(datetime(2026, 9, 5, 17, 40)), "sources": [source_podcast]},
    {"word": "vocabulary", "translation": "vocabulaire", "explainations": None,
     "mastered": False, "added": timezone.make_aware(datetime(2026, 9, 8, 9, 50)), "sources": [source_podcast]},
    {"word": "whimsical", "translation": "fantasque / loufoque", "explainations": "Décrit quelque chose d'espiègle et d'imaginatif.",
     "mastered": False, "added": timezone.make_aware(datetime(2026, 9, 12, 12, 0)), "sources": [source_hp, source_lotr]},
    {"word": "riddle", "translation": "énigme", "explainations": None,
     "mastered": True, "added": timezone.make_aware(datetime(2026, 9, 15, 15, 25)), "sources": [source_hp]},
    {"word": "overwhelmed", "translation": "submergé / dépassé", "explainations": "Émotion forte, positive ou négative.",
     "mastered": False, "added": timezone.make_aware(datetime(2026, 9, 18, 21, 15)), "sources": [source_strangerthings, source_inception]},
    {"word": "ancient", "translation": "ancien / antique", "explainations": None,
     "mastered": True, "added": timezone.make_aware(datetime(2026, 9, 19, 10, 0)), "sources": [source_lotr]},
]

for w in words_data:
    sources = w.pop("sources")
    word_obj, created = Word.objects.get_or_create(word=w["word"], defaults=w)
    word_obj.sources.set(sources)
    print(f"{'Cree' if created else 'Deja present'} : {word_obj}")

print("Peuplement termine.")
print(f"Total mots : {Word.objects.count()}")
print(f"Total sources : {Source.objects.count()}")
print(f"Total auteurs : {Author.objects.count()}")