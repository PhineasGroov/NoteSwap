from django.contrib import admin
from .models import Note, NoteRating, NoteComment


# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploader', 'subject', 'course', 'semester', 'uploaded_at')
    search_fields = ('title', 'subject', 'course', 'semester', 'uploader__username')

admin.site.register(NoteRating)
admin.site.register(NoteComment)