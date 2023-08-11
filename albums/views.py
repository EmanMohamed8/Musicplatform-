from rest_framework import status, pagination
from rest_framework.views import APIView
from .serializers import AlbumSerializers
from rest_framework.response import Response
from .models import Album, Artist
from django.db.models import Q


class AlbumPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    max_limit = 10


class AlbumsList(APIView):
    pagination_class = AlbumPagination

    def get(self, request):
        albums = Album.objects.filter(approved=True)

        cost_gte = request.query_params.get('cost__gte')
        cost_lte = request.query_params.get('cost__lte')
        name = request.query_params.get('name')
        if cost_lte is not None:
            albums = albums.filter(cost__lte=cost_lte)
        if cost_gte is not None:
            albums = albums.filter(cost__gte=float(cost_gte))
        if name is not None:
            albums = albums.filter(Q(name__icontains=name))
        paginator = self.pagination_class()
        paginated_albums = paginator.paginate_queryset(albums, request)
        serializer = AlbumSerializers(paginated_albums, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication credentials were not provided."}, status=status.HTTP_403_FORBIDDEN)
        try:
            artist = request.user.artist
        except Artist.DoesNotExist:
            return Response({"error": "Authentication credentials were not provided."}, status=status.HTTP_403_FORBIDDEN)
        serializer = AlbumSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(artist=artist)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status=status.HTTP_400_BAD_REQUEST
        )


class CustomAlbums(APIView):
    pagination_class = AlbumPagination

    def get(self, request):
        albums = Album.objects.filter(approved=True)

        cost_gte = request.query_params.get('cost__gte')
        cost_lte = request.query_params.get('cost__lte')
        name = request.query_params.get('name')
        if cost_lte is not None:
            try:
                cost_lte = float(cost_lte)
                albums = [album for album in albums if album.cost <= cost_lte]
            except ValueError:
                return Response({'error': 'Invalid data type for cost__lte filter.'}, status=status.HTTP_400_BAD_REQUEST)
        if cost_gte is not None:
            try:
                cost_gte = float(cost_gte)
                albums = [album for album in albums if album.cost >= cost_gte]
            except ValueError:
                return Response({'error': 'Invalid data type for cost__gte filter.'}, status=status.HTTP_400_BAD_REQUEST)
        if name is not None:
            albums = [album for album in albums if album.name.lower()
                      == name.lower()]

        paginator = self.pagination_class()
        paginated_albums = paginator.paginate_queryset(albums, request)
        serializer = AlbumSerializers(paginated_albums, many=True)
        return paginator.get_paginated_response(serializer.data)
