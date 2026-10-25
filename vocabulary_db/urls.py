from django.urls import include, path
  
from . import views
  
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),

    path('list/words', views.WordsList.as_view(), name="words"),
    path('flashcards', views.WordsFlashcards.as_view(), name="flashcards"),
    path('flashcards/mastering/<pk>', views.ToggleMastered.as_view(), name='toggle_mastered'),
    path('add/word', views.AddWord.as_view(), name="add_word"),
    path('edit/word/<str:pk>', views.EditWord.as_view(), name="edit_word"),
    path('delete/word/<str:pk>', views.DeleteWord.as_view(), name="delete_word"),

    path('source/<int:pk>', views.SourceInfo.as_view(), name="source"),
    path('list/sources', views.SourcesList.as_view(), name="sources"),
    path('add/source', views.AddSource.as_view(), name="add_source"),
    path('edit/source/<int:pk>', views.EditSource.as_view(), name="edit_source"),
    path('delete/source/<int:pk>', views.DeleteSource.as_view(), name="delete_source"),
    
    path('list/types', views.TypesList.as_view(), name="types"),
    path('add/author', views.AddAuthor.as_view(), name="add_author"),
    path('edit/author/<int:pk>', views.EditAuthor.as_view(), name="edit_author"),
    path('delete/author/<int:pk>', views.DeleteAuthor.as_view(), name="delete_author"),
    
    path('list/authors', views.AuthorsList.as_view(), name="authors"),
    path('add/type', views.AddType.as_view(), name="add_type"),
    path('edit/type/<int:pk>', views.EditType.as_view(), name="edit_type"),
    path('delete/type/<int:pk>', views.DeleteType.as_view(), name="delete_type"),

    # not implemented ↓
    path('stats', views.WordsList.as_view(), name="stats"),
]