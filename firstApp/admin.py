from django.contrib import admin
from django.utils.html import mark_safe
from . models import Teacher

# Register your models here.

@admin.register(Teacher)
class Teacher (admin.ModelAdmin):
    list_display =('name','roll', 'phone', 'address','image_tag',)
    search_fields = ('name','t_id')



    def image_tag(self, obj):
        if obj.image:
            return mark_safe('<img src="{0}" width="150" height="150" style="object-fit:contain" />'.format(obj.image.url))
        else:
            return '(No image)'
        
    image_tag.short_description = 'image'