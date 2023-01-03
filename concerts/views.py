from rest_framework import generics
from .models import Concert, Venue, Artist
from .serializers.concert_serializer import ConcertSerializer


class ConcertList(generics.ListAPIView):
    serializer_class = ConcertSerializer

    def get_queryset(self):
        queryset = Concert.objects.all()
        artist = self.request.query_params.get("artist")
        venue = self.request.query_params.get("venue")

        if venue is not None:
            queryset = queryset.filter(venue__id=venue)

        if artist is not None:
            queryset = queryset.filter(act__artist__id=artist)

        return queryset


class ConcertDetail(generics.RetrieveAPIView):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer
