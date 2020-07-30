from django.contrib import admin
from .models import (
    Country, Province, City, Tribe, Major, Gender
    )

admin.site.register(Gender)

@admin.register(Country)
class Roles(admin.ModelAdmin):
    list_display = ('country_code', 'country_desc')
    ordering = ('country_desc',)
    search_fields = ['country_code', 'country_desc']

@admin.register(Province)
class Roles(admin.ModelAdmin):
    list_display = ('province_code', 'province_desc')
    ordering = ('province_desc',)
    search_fields = ['province_code', 'province_desc']

@admin.register(City)
class Roles(admin.ModelAdmin):
    list_display = ('city_code', 'city_desc')
    ordering = ('city_desc',)
    search_fields = ['city_code', 'city_desc']


#custom admin
@admin.register(Tribe)
class Tribe(admin.ModelAdmin):
    list_display = ('tribe_code', 'tribe_desc')
    ordering = ('tribe_desc',)
    search_fields = ['tribe_code', 'tribe_desc']

@admin.register(Major)
class Major(admin.ModelAdmin):
    list_display = ('major_code', 'major_desc')
    ordering = ('major_desc',)
    search_fields = ['major_code', 'major_desc']

# @admin.register(Organization)
# class Organization(admin.ModelAdmin):
#     list_display = ('user', 'title')
#     ordering = ('title',)
#     search_fields = ['user', 'title']
