from django.contrib import admin
from .models import Note, Student, PersonalNote #

class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

# Register your models here.
admin.site.register(Note, NoteAdmin) #
admin.site.register(PersonalNote) #
admin.site.register(Student, StudentAdmin) #