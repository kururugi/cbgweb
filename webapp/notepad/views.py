from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from models import Note

def noteView(request, noteid):
    note = get_object_or_404(Note, pk=noteid)
    print note.text
    return HttpResponse(note.text, content_type="text/plain")
