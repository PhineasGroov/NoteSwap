from django.urls import path
from . import views
from .views import NoteAPI

urlpatterns = [
    path('', views.home, name='home'),  # page d'accueil publique
    path('upload/', views.upload_note, name='upload_note'),
    path('api/', NoteAPI.as_view(), name='note_api'),
    path('note_list/', views.note_list, name='note_list'),  # accès réservé
    path('api/<int:note_id>/rate/', views.rate_note, name='rate_note'),
    path('api/<int:note_id>/comment/', views.comment_note, name='comment_note'),
    path('api/note/<int:note_id>/delete/', views.ajax_delete_note, name='ajax_delete_note'),
    path('api/note/<int:note_id>/edit/', views.ajax_edit_note, name='ajax_edit_note'),
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
]