from django.urls import include, path
  
from . import views
  
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),

    path('list/words', views.WordsList.as_view(), name="words"),
    path('list/sources', views.SourcesList.as_view(), name="sources"),
    path('list/authors', views.AuthorsList.as_view(), name="authors"),
    path('list/types', views.TypesList.as_view(), name="types"),
    # not implemented ↓
    path('stats', views.WordsList.as_view(), name="stats"),

    path('source/<int:pk>', views.SourceInfo.as_view(), name="source"),
    

    path('add/word', views.AddWord.as_view(), name="add_word"),
    path('add/source', views.AddSource.as_view(), name="add_source"),
    path('add/author', views.AddAuthor.as_view(), name="add_author"),
    path('add/type', views.AddType.as_view(), name="add_type"),

    path('edit/word/<str:pk>', views.EditWord.as_view(), name="edit_word"),
    path('edit/source/<int:pk>', views.EditSource.as_view(), name="edit_source"),
    path('edit/author/<int:pk>', views.EditAuthor.as_view(), name="edit_author"),
    path('edit/type/<int:pk>', views.EditType.as_view(), name="edit_type"),

    path('delete/word/<str:pk>', views.DeleteWord.as_view(), name="delete_word"),
    path('delete/source/<int:pk>', views.DeleteSource.as_view(), name="delete_source"),
    path('delete/author/<int:pk>', views.DeleteAuthor.as_view(), name="delete_author"),
    path('delete/type/<int:pk>', views.DeleteType.as_view(), name="delete_type"),
]