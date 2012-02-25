from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404

from blog.models import Entry
from notepad.models import Note

def home_index(request):
    entries = Entry.objects.order_by('-pub_date')[0:5]
    template = loader.get_template('pages/index.html')
    context = RequestContext(request, {'articles': entries})
    return HttpResponse(template.render(context))

def contribute(request):
    content = get_object_or_404(Note, pk=3)
    template = loader.get_template('pages/contribute.html')
    context = RequestContext(request, {'content': content.text, 'contribute': True})
    return HttpResponse(template.render(context))
