from django.contrib import admin

# Register your models here.

from .models import Album, Song, TariffDetail, Item

admin.site.register(Album)
admin.site.register(Song)

class TariffDetailAdmin(admin.ModelAdmin):
    ordering = ["-subheadingCode"]

    list_display = (
        "id",
        "isSubChapter",
        "isSubHeading",
        "subheadingCode",
        "parent_id",
        "description",
        "isHeading",
        "headingCode",
        "unitOfQty",
        "rate",
        "orderRank",
        "deleted",
        "updated_at",
    )
admin.site.register(TariffDetail, TariffDetailAdmin)
#admin.site.register(TariffDetail)
admin.site.register(Item)

