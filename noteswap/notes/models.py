from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='notes/')
    subject = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    semester = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)  # Explicitly define the primary key if needed

    def __str__(self):
        return self.title
    
class NoteRating(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('note', 'user')

class NoteComment(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.note.title}'