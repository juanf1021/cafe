from .models import Blog
from django.contrib import admin

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    readonly_fields=('fecha',)

admin.site.register(Blog, BlogAdmin)