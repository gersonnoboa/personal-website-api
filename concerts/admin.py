from django.contrib import admin
from .models import Artist, Concert, Country, Venue, Act

admin.site.register(Artist)
admin.site.register(Concert)
admin.site.register(Country)
admin.site.register(Venue)
admin.site.register(Act)
