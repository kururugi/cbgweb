from notepad.models import Note
from django.contrib import admin

class NotepadAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'timestamp', 'id')

admin.site.register(Note, NotepadAdmin)
