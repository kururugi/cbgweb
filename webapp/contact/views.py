from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext, Context
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
import forms

#####################
#   Contact Page    #
#####################

def contact(request):
    data = None
    if request.method == 'POST': # If the form has been submitted...
        data = request.POST
        form = forms.ContactForm(data) # A form bound to the POST data
        if form.is_valid():
            try:
                send_mail(
                    "AUTO: cloudbyte.com user regarding: " + form.cleaned_data['attention'],
                    "Message from %s:\n%s" % (form.cleaned_data['visitor_address'], form.cleaned_data['message']),
                    form.cleaned_data['visitor_address'],
                    ['zer000.cloudbyte@gmail.com'],
                    fail_silently=False
                )
            except Exception, e:
                print e
                return HttpResponseRedirect(reverse('info_output', kwargs={'msgtype': 'senterr', 'redirect': 'contact-index'}))
            return HttpResponseRedirect(reverse('info_output', kwargs={'msgtype': 'sent', 'redirect': 'contact-index'}))
    template = loader.get_template('pages/contact.html')
    form = forms.ContactForm(data)
    context = RequestContext(request, {'contact_form': form})
    return HttpResponse(template.render(context))
