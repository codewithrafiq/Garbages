# from django.contrib import admin
from django.contrib.gis import admin
from .models import Location,District,Country
from leaflet.admin import LeafletGeoAdmin


# class LocationAdmin(admin.OSMGeoAdmin):
class LocationAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')
    search_fields = ('name',)
class AreaAdmin(LeafletGeoAdmin):
    list_display = ('adm0_en', 'adm1_en')
class CountryAdmin(LeafletGeoAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Location, LocationAdmin)
admin.site.register(District, AreaAdmin)
admin.site.register(Country, CountryAdmin)

