from django.http import HttpResponse
from django.template import loader, RequestContext
from django.core.paginator import Paginator
from django.http import Http404
from models import *

def blog_index(request, page=None):
    page = 1 if page==None else page
    articles = Entry.objects.all()
    p = Paginator(articles, 3)
    try:
        displaypage = p.page(page)
    except:
        raise Http404
    print "number of pages: ", p.num_pages
    print "has previous: ", displaypage.has_previous()
    template = loader.get_template('blog/blog.html')
    context = RequestContext(request, {"page": displaypage, "news": True})
    return HttpResponse(template.render(context))

def blog_archive(request):
    pass
