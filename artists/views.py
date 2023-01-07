from django.shortcuts import render
from albums.models import Album
from .models import Artist
from django.urls import reverse
from django.db.models import Count
from django.views.generic import CreateView, ListView
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import ArtistSerializers
from django.http.response import JsonResponse
from rest_framework.response import Response
from django .http import Http404


class ArtistList(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializers(artists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArtistSerializers(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status=status.HTTP_400_BAD_REQUEST
        )


class ArtistPk(APIView):
    def get_object(self, pk):
        try:
            return Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            raise Http404

    def get(self, requset, pk):
        artists = self.get_object(pk)
        serializer = ArtistSerializers(artists)
        return Response(serializer.data)

    def put(self, requset, pk):
        artists = self.get_object(pk)
        serializer = ArtistSerializers(artists, data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requset, pk):
        artists = self.get_object(pk)
        artists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
