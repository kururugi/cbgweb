from django.http import HttpResponse
from django.template import loader, RequestContext

def home_index(request):
    template = loader.get_template('pages/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
