from django.db import models

class Entry(models.Model):
    headline = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField()

    class Meta:
        db_table = 'blog_entry'
        verbose_name_plural = 'entries'
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'

    def __unicode__(self):
        return self.headline

# Optional support for tags (django-tagging)
try:
    import tagging
    tagging.register(Entry)
except ImportError:
    pass
