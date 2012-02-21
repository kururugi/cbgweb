from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.core.urlresolvers import reverse

def info_message(request, msgtype, redirect=None):
    STANDARD_MESSAGES = {
        "acctdsbl": ("Your account was disabled.", "error"),
        "badlogin": ("Login incorrect. Please try again", "error"),
        "sent": ("Your email was delivered successfully, thank you.", "normal"),
        "senterr": ("There was an error in sending your email. Please try again another time.", "error"),
    }
    if not msgtype in STANDARD_MESSAGES.keys():
        return HttpResponseRedirect('/')
    nexturl = "homepage-index" if redirect==None else redirect
    template = loader.get_template('global/message.html')
    context = Context({
        'next_page': reverse(nexturl),
        'message_type': STANDARD_MESSAGES[msgtype][1],
        'message': STANDARD_MESSAGES[msgtype][0]
    })
    return HttpResponse(template.render(context))
