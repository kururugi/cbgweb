from django.http import HttpResponse
from django.template import loader, RequestContext

from blog.models import Entry

def home_index(request):
    entries = Entry.objects.order_by('-pub_date')[0:5]
    template = loader.get_template('pages/index.html')
    context = RequestContext(request, {'articles': entries})
    return HttpResponse(template.render(context))
