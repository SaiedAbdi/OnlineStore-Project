from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category, CategoryAdmin)




class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','available')
    list_filter = ('available','created')
    list_editable = ('price','available')
    prepopulated_fields = {'slug':('name',)}
    raw_id_fields = ('category',)
    actions = ('make_available',)

    def make_available(self, request, queryset):
        rows = queryset.update(available=True)
        self.message_user(request, f'{rows} updated')
    make_available.short_description = 'make all available'

admin.site.register(Product, ProductAdmin)