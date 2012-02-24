from django.http import HttpResponse
from django.template import loader, RequestContext
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
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
    template = loader.get_template('blog/blog.html')
    context = RequestContext(request, {"page": displaypage, "news": True})
    return HttpResponse(template.render(context))

def article_detail(request, articleid):
    article = get_object_or_404(Entry, pk=articleid)
    template = loader.get_template('blog/detail.html')
    context = RequestContext(request, {"article": article, "news": True})
    return HttpResponse(template.render(context))

def blog_archive(request):
    pass
