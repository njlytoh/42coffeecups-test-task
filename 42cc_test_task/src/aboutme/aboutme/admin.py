from django.contrib import admin

from aboutme.models import AboutMe



class AboutMeAdmin(admin.ModelAdmin):
    list_display = ( 'given_name', 'family_name', 'cell_phone') 
    search_fields = ('given_name', 'family_name', 'middle_name')
    fieldsets = [
                   ('Name',               {'fields': ['given_name', 'middle_name', 'family_name']}),
                   ('Contact details',    {'fields': ['cell_phone', 'home_phone']}),
                   ('Biography',          {'fields': ['bio']}),
                ]

admin.site.register(AboutMe, AboutMeAdmin)

