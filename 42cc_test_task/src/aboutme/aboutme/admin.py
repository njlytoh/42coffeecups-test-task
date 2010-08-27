from django.contrib import admin

from aboutme.models import AboutMe



class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'description')
    search_fields = ('name', 'title', 'description')

admin.site.register(AboutMe, AboutMeAdmin)

