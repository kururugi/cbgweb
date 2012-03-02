from django.db import models

class Entry(models.Model):
    text = models.TextField()
    author = models.TextField()
    parent = models.IntegerField()
    num_votes = models.IntegerField()
    karma = models.IntegerField()
    karma_ratio = models.FloatField()
    pub_date = models.DateTimeField()
    
    class Meta:
        db_table = 'faq_entry'
        verbose_name_plural = 'entries'
        ordering = ('-karma_ratio',)
        get_latest_by = 'pub_date'
    def __unicode__(self):
        return self.question
        
try:
    import tagging
    tagging.register(Entry)
except ImportError:
    pass
    