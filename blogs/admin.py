from django.contrib import admin

from blogs.models import AuthorModel, BlogCategoryModel, BlogModel, BlogTagModel


@admin.register(AuthorModel)
class AuthorModel(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_filter = ('name', 'created_at',)
    search_fields = ('name',)


@admin.register(BlogCategoryModel)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_filter = ('name', 'created_at',)
    search_fields = ('name',)


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at',)
    list_filter = ('created_at',)
    search_fields = ('title', 'content',)


@admin.register(BlogTagModel)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_filter = ('name',)
    search_fields = ('name', 'created_at',)
