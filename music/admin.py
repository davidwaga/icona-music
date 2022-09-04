from django.contrib import admin

# Register your models here.

from .models import Album, Song, TariffDetail, Item

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(TariffDetail)
admin.site.register(Item)

