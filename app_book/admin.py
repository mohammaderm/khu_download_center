from django.contrib import admin
from app_book.models import Book, Category, Files, Blogbook
# Register your models here.


admin.site.register(Category)
admin.site.register(Blogbook)


class FilesAdmin(admin.StackedInline):
    model = Files


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [FilesAdmin]


@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    pass
