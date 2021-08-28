
from .models import Category
from django.contrib import admin




class CategoryAdmin(admin.ModelAdmin):
    """Setting for the Category model"""

    prepopulated_fields = {
        'slug':('category_name',)
    }
    list_display = ('id', 'category_name', 'slug', 'description')
    list_display_links = ('category_name',)



# Register your models here.

admin.site.register(Category, CategoryAdmin)

# admin.site.register(CategoryAdmin)