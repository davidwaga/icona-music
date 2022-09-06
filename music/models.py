from django.contrib.auth.models import Permission, User
from django.db import models


class Album(models.Model):
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title



class TariffDetail(models.Model):
    isSubChapter = models.BooleanField(default=False)
    isHeading = models.BooleanField(default=False)
    isSubHeading = models.BooleanField(default=False)
    parent_id = models.IntegerField(null=True, blank=True)
    headingCode = models.CharField(max_length=512, null=True)
    subheadingCode = models.CharField(max_length=250)
    description = models.TextField(blank=True, max_length=512, null=True)
    unitOfQty = models.CharField(max_length=512, null=True, blank=True)
    rate = models.FloatField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    orderRank = models.PositiveIntegerField(blank=False, null=True)

    def __str__(self):
        return self.subheadingCode
    
    class Meta:
        verbose_name = "TariffDetail"
        verbose_name_plural = "TariffDetails"


class Item(models.Model):
    tariff_detail = models.ForeignKey(TariffDetail, on_delete=models.CASCADE, null=True, blank=False, verbose_name="Subheading")
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, max_length=512)
    appliedGir = models.CharField(max_length=512, blank=False, null=True)
    considerationStep = models.TextField(max_length=512)
    deleted = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    orderRank = models.PositiveIntegerField(blank=False, null=True)
    remarks = models.TextField(blank=True, null=True, max_length=512)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Guideline"
        verbose_name_plural = "Guideline"