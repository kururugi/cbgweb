from django.db import models

class Note(models.Model):
    timestamp = models.DateField(auto_now=True)
    text = models.TextField()
    def __unicode__(self):
        return "<Note edited: %s >" % self.timestamp
