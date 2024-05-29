from django.contrib import admin
from .models import Client, NewsLetterContent, NewsLetterEmail


class ClientAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Client model.
    """
    list_display = ('id', 'name', 'email', 'phone_number')


class NewsLetterContentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the NewsLetterContent model.
    """
    list_display = ('id', 'date_created')


class NewsLetterEmailAdmin(admin.ModelAdmin):
    """
    Admin configuration for the NewsLetterEmail model.
    """
    list_display = ('id', 'email')


admin.site.register(Client, ClientAdmin)
admin.site.register(NewsLetterContent, NewsLetterContentAdmin)
admin.site.register(NewsLetterEmail, NewsLetterEmailAdmin)
