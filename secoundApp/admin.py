from django.contrib import admin
from django.utils.html import mark_safe
from . models import Student

# Register your models here.

@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display =('name','roll', 'phone', 'address', 'image_tag',)
    search_fields = ('name',)


    def image_tag(self, obj):
        if obj.image:
            return mark_safe('<img src="{0}" width="50" height="50" style="object-fit:contain" />'.format(obj.image.url))
        else:
            return '(No image)'
        
    image_tag.short_description = 'image'