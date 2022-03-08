from django.contrib import admin

from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name_inenglish',)}
    list_display = ('category_name_inarabic','category_name_inenglish', 'slug')

admin.site.register(Category, CategoryAdmin)