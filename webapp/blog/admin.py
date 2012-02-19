from django.contrib import admin
from models import *

try:
    import tagging

    Tag = tagging.models.Tag

    def tag_devel(modeladmin, request, queryset):
        for entry in queryset:
            Tag.objects.add_tag(entry, 'devel')
    tag_devel.short_description = "Tag selected entries with 'devel'"

    def untag_devel(modeladmin, request, queryset):
        for entry in queryset:
            start, _, end = entry.tags.partition('devel')
            if not end:
                continue
            entry.tags = '%s %s' % (start.strip(), end.strip())
            entry.save()
    untag_devel.short_description = "Remove 'devel'-tag from selected entries"

except ImportError:
    tag_devel = None

class EntryAdmin(admin.ModelAdmin):
    model = Entry
    list_display = ('headline', 'pub_date')
    date_hierarchy = 'pub_date'
    search_fields = ('headline', 'content')
    if tag_devel:
        actions = [tag_devel]
        #actions = [tag_devel, untag_devel]

admin.site.register(Entry, EntryAdmin)
