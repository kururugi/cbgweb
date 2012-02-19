from django.http import HttpResponse
from django.template import loader, RequestContext
from models import *

def blog_index(request):
    articles = Entry.objects.all()
    template = loader.get_template('blog/test.html')
    context = RequestContext(request, {"articles": articles})
    return HttpResponse(template.render(context))
