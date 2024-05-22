from django.contrib import admin

from products.models import ProductsModel, ProductsCategoryModel, ProductTagModel


@admin.register(ProductsModel)
class ProductsModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'price', 'description',)
    list_filter = ('created_at',)
    search_fields = ('name', 'content',)


@admin.register(ProductsCategoryModel)
class ProductsCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_filter = ('name', 'created_at',)
    search_fields = ('name',)


@admin.register(ProductTagModel)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_filter = ('name',)
    search_fields = ('name', 'created_at',)
