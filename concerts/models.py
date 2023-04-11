from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image_url = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Venue(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Concert(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default=None, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(default=None, blank=True, null=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self) -> str:
        return f"Venue: {self.venue}, on date: {self.start_date}"


class Act(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    setlist_url = models.CharField(max_length=400, blank=True, null=True)
    is_main = models.BooleanField()
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.artist.name} in {self.concert.venue.name}"
