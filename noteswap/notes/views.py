from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NoteForm
from .models import Note, NoteRating, NoteComment
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.db import models
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponseForbidden
from .forms import NoteForm
import json

@method_decorator(csrf_exempt, name='dispatch')
class NoteAPI(View):
    def get(self, request):
        notes = Note.objects.all().order_by('-uploaded_at')
        subject = request.GET.get('subject')
        course = request.GET.get('course')
        semester = request.GET.get('semester')
        search = request.GET.get('search')

        if subject:
            notes = notes.filter(subject__icontains=subject)
        if course:
            notes = notes.filter(course__icontains=course)
        if semester:
            notes = notes.filter(semester__icontains=semester)
        if search:
            notes = notes.filter(
                models.Q(title__icontains=search) |
                models.Q(subject__icontains=search) |
                models.Q(course__icontains=search) |
                models.Q(semester__icontains=search)
            )
            
        notes_data = [
            {
                'id': note.id,
                'title': note.title,
                'subject': note.subject,
                'course': note.course,
                'semester': note.semester,
                'uploader': note.uploader.username,
                'uploaded_at': note.uploaded_at.strftime('%Y-%m-%d %H:%M'),
                'file_url': note.file.url,
                'avg_rating': note.ratings.aggregate(models.Avg('value'))['value__avg'] or 0,
                'comments': [
                    {
                        'user': comment.user.username,
                        'text': comment.text,
                        'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')
                    }
                    for comment in note.comments.order_by('created_at')
                ]
            }
            for note in notes
        ]
        return JsonResponse({'notes': notes_data})

    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required.'}, status=403)
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.uploader = request.user
            note.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.uploader = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/upload_note.html', {'form': form})

@login_required
def note_list(request):
    notes = Note.objects.all().order_by('-uploaded_at')
    return render(request, 'notes/note_list.html', {'notes': notes})

@csrf_exempt
@require_POST
def rate_note(request, note_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required.'}, status=403)
    value = int(request.POST.get('value', 0))
    if value < 1 or value > 5:
        return JsonResponse({'error': 'Invalid rating.'}, status=400)
    note = Note.objects.get(id=note_id)
    rating, created = NoteRating.objects.update_or_create(
        note=note, user=request.user, defaults={'value': value}
    )
    avg_rating = note.ratings.aggregate(models.Avg('value'))['value__avg']
    return JsonResponse({'success': True, 'avg_rating': avg_rating})

@csrf_exempt
@require_POST
def comment_note(request, note_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required.'}, status=403)
    text = request.POST.get('text', '').strip()
    if not text:
        return JsonResponse({'error': 'Empty comment.'}, status=400)
    note = Note.objects.get(id=note_id)
    comment = NoteComment.objects.create(note=note, user=request.user, text=text)
    return JsonResponse({
        'success': True,
        'comment': {
            'user': comment.user.username,
            'text': comment.text,
            'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')
        }
    })
@login_required
@require_POST
def ajax_delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, uploader=request.user)
    note.delete()
    return JsonResponse({'success': True})

@login_required
@require_POST
def ajax_edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, uploader=request.user)
    form = NoteForm(request.POST, request.FILES, instance=note)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'notes/note_detail.html', {'note': note})

def home(request):
    if request.user.is_authenticated:
        from django.shortcuts import redirect
        return redirect('note_list')
    return render(request, 'notes/home.html')