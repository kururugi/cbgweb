from datetime import datetime, timedelta

from django.template.loader import render_to_string

from blog.models import Entry as _Entry

_five_minutes = timedelta(seconds=5*60)

def add_entry_to_blog(object, headline, template, date_field='last_modified'):
    data = {'obj': object}
    current_time = datetime.now()
    template = render_to_string(template, dictionary=data)
    pub_date = object.__dict__.get(date_field, current_time)
    latest = _Entry.objects.latest()
    # Prevent duplicates
    if not (latest.headline == headline and latest.pub_date > current_time - _five_minutes):
        blog_entry = _Entry.objects.create(content=template,headline=headline,pub_date=pub_date)
        return blog_entry
