from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.getorCreateNotes, name="get-or-create-notes"),
    path('notes/<str:id>', views.getorModifyNote, name="get-or-modify-note"),
    # path('create-notes/', views.createNote, name="create-note"),
    # path('update-notes/<str:id>', views.updateNote, name="update-note"),
    # path('delete-notes/<str:id>', views.deleteNote, name="delete-note"),
]