from django.contrib import admin
from .models import Note
# Register your models here.

# admin.site.register(admin.ModelAdmin):

class CustomNote(admin.ModelAdmin):
    list_display = ['title','content','created_at','updated_at']
    search_fields = ['title']

admin.site.register(Note,CustomNote)


