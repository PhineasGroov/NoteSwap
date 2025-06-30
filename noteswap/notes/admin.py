from django.contrib import admin
from .models import Note, NoteRating, NoteComment


# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploader', 'subject', 'course', 'semester', 'uploaded_at')
    search_fields = ('title', 'subject', 'course', 'semester', 'uploader__username')
    list_filter = ('subject', 'course', 'semester', 'uploaded_at')
    date_hierarchy = 'uploaded_at'
    autocomplete_fields = ['uploader']


@admin.register(NoteRating)
class NoteRatingAdmin(admin.ModelAdmin):
    list_display = ('note', 'user', 'value')
    search_fields = ('note__title', 'user__username')


@admin.register(NoteComment)
class NoteCommentAdmin(admin.ModelAdmin):
    list_display = ('note', 'user', 'text', 'created_at')
    search_fields = ('note__title', 'user__username', 'text')
    list_filter = ('created_at',)