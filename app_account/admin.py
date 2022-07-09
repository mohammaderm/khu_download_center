from django.contrib import admin
from app_account.models import Profile, Softrequest
# Register your models here.


class SoftrequestAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'softname',
        'description',
        'request_status',
        'publish_date',

    )
    search_fields = ('user', 'softname',)
    list_filter = ('softname', 'user', 'request_status',)


admin.site.register(Softrequest, SoftrequestAdmin)
admin.site.register(Profile)
