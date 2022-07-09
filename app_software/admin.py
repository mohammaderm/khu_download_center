from django.contrib import admin

from app_software.models import Software, Category, File_Software, Blogsoft

# Register your models here.
admin.site.register(Category)
admin.site.register(Blogsoft)


class File_SoftwareAdmin(admin.StackedInline):
    model = File_Software


@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    inlines = [File_SoftwareAdmin]


@admin.register(File_Software)
class File_SoftwareAdmin(admin.ModelAdmin):
    pass
