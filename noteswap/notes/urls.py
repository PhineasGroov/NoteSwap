from django.urls import path
from . import views
from .views import NoteAPI

urlpatterns = [
    path('upload/', views.upload_note, name='upload_note'),
    path('api/', NoteAPI.as_view(), name='note_api'),
    path('', views.note_list, name='note_list'),
    path('api/<int:note_id>/rate/', views.rate_note, name='rate_note'),
    path('api/<int:note_id>/comment/', views.comment_note, name='comment_note'),
    
]