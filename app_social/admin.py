from django.contrib import admin
from app_social.models import Cumment, Cummentlike, Like, Bookmark
# Register your models here.


class BookmarkAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'content_object',
    )


class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'content_object',
    )


class CummentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'content_object',
        'value',
        'validation',
    )
    search_fields = ('value',)
    list_filter = ('content_type', 'validation',)


admin.site.register(Like, LikeAdmin)
admin.site.register(Cumment, CummentAdmin)
admin.site.register(Cummentlike)
admin.site.register(Bookmark, BookmarkAdmin)
