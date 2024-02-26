from django.contrib import admin
from .models import Post, Category, Android_Post, Type

# admin.site.register(Post) . if you want to register the model with the default admin interface

@admin.register(Post) # if you want to register the model with the custom admin interface
class PostAdmin(admin.ModelAdmin): 
    list_display = ['title', 'slug', 'date']
    list_filter = ['title', 'date']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['date']

@admin.register(Category) # if you want to register the model with the custom admin interface
class CategoryAdmin(admin.ModelAdmin): 
    list_display = ['name']
    search_fields = ['name']

@admin.register(Android_Post)
class Android_PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'type']
    list_filter = ['type']
    search_fields = ['title']
    ordering = ['title']

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']