from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance, Language, item

admin.site.register(Book)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
admin.site.register(Author, AuthorAdmin)



admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Language)




class ItemAdmin(admin.ModelAdmin):
    list_display = ('Sku', 'name', 'price', 'weight')
admin.site.register(item, ItemAdmin)