from django.contrib import admin
from .models import BB, Classification

# стер published из list_display

class BBAdmin(admin.ModelAdmin):
    list_display = ('name','classification', 'description', 'price')
    list_display_links = ('name', 'description')
    search_fields = ('classification','name', 'description')

admin.site.register(BB,BBAdmin)
admin.site.register(Classification)

# Register your models here.
