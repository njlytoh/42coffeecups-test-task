from django.contrib import admin

from aboutme.models import AboutMe



class AboutMeAdmin(admin.ModelAdmin):
    list_display = ( 'given_name', 'family_name', 'cell_phone') 
    search_fields = ('given_name', 'family_name', 'middle_name')

admin.site.register(AboutMe, AboutMeAdmin)

