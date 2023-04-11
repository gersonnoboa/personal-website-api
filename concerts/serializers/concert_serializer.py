from ..models import Concert, Act, Artist, Venue, Country
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = ['name']

class VenueSerializer(serializers.ModelSerializer):
	country = CountrySerializer()
	class Meta:
		model = Venue
		fields = ['name', 'id', 'country']

class ArtistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artist
		fields = ['name', 'id', 'image_url']

class ActSerializer(serializers.ModelSerializer):
	artist = ArtistSerializer()

	class Meta:
		model = Act
		fields = ['setlist_url', 'artist', 'is_main']


class ConcertSerializer(serializers.ModelSerializer):
	act_set = ActSerializer(many=True)
	venue = VenueSerializer()

	class Meta:
		model = Concert
		fields = ['start_date', 'end_date', 'name', 'venue', 'act_set']
