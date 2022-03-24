from django.contrib import admin

from .models import Category, HomeSliedes, MasterCategory

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name_inenglish',)}
    list_display = ('category_name_inarabic','category_name_inenglish', 'slug')

admin.site.register(Category, CategoryAdmin)



class AdminHomeSliedes(admin.ModelAdmin):
    list_display = ('title','description')



class AdminMasterCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name_inenglish',)}
    list_display = ('category_name_inarabic','category_name_inenglish', 'slug')

admin.site.register(HomeSliedes, AdminHomeSliedes)
admin.site.register(MasterCategory, AdminMasterCategory)