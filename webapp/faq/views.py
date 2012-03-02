from django.http import HttpResponse
from django.template import loader, RequestContext
from django.template import Library

from faq.models import Entry
import forms

from datetime import datetime

from random import randint

indent_size = 50
def getEntryChildren(entry,level):
    lst = []
    children = Entry.objects.all().filter(parent=entry.id)
    for child in children:
        child.level = level
        lst.append(child)
        lst.extend(getEntryChildren(child,level+indent_size))
    return lst

def faq_index(request):
    entries = Entry.objects.all().filter(parent=0)
    finalEntryList = []
    for entry in entries:
        finalEntryList.append(entry)
        entry.level = 15
        finalEntryList.extend(getEntryChildren(entry,15 + indent_size))
    template = loader.get_template('faq/faq.html')
    context = RequestContext(request, {'entries': finalEntryList})
    return HttpResponse(template.render(context))
def faq_vote(request):
    if request.method == "GET":#TODO switch to post
        data = request.GET
        form = forms.Vote(data)
        if (form.is_valid()):
            a = Entry.objects.get(id=form.cleaned_data['id'])
            if (form.cleaned_data["vote"] == 1):
                a.karma += 1
            else:
                a.karma -= 1
            a.num_votes += 1
            if (a.num_votes < 20):
                a.karma_ratio = (a.num_votes + a.karma) * 1.0 / ((a.num_votes - a.karma) or 0.01) * (a.num_votes / 20.0)
            else:
                a.karma_ratio = (a.num_votes + a.karma) * 1.0 / ((a.num_votes - a.karma) or 0.01)
            a.save()
    return HttpResponse()
def faq_newreply(request):
    if request.method == "GET":#TODO switch to post
        data = request.GET
        form = forms.NewReply(data)
        #TODO This should be cleaned of any html
        if (form.is_valid()):
            a = Entry(text = form.cleaned_data['text'],
                      karma = 1,
                      karma_ratio=0,
                      pub_date=datetime.now(),
                      num_votes=1,
                      parent = form.cleaned_data['parent'],
                      author = form.cleaned_data['author'],)
            a.save()
    return HttpResponse("success")#Success/Failure Codes?
#Remove after implementing a comment adding system
def faq_test(request):
    uv = randint(0,500)
    dv = randint(0,500)
    a = Entry(text=getRandomText(randint(15,300)),
              author=getRandomText(randint(3,15)),
              parent=0,
              num_votes=uv+dv,
              karma=uv-dv,
              karma_ratio=uv/dv,
              pub_date=datetime.now())
    a.save()
letters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def getRandomText(length):
    string = ""
    for i in range(length):
        if (randint(0,10)<2):
            string += " "
        else:
            string += letters[randint(0,len(letters)-1)]
    return string