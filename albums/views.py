from rest_framework import status, pagination
from rest_framework.views import APIView
from .serializers import AlbumSerializers
from rest_framework.response import Response
from .models import Album


class AlbumPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    max_limit = 10


class AlbumsList(APIView):
    pagination_class = AlbumPagination

    def get(self, request):
        albums = Album.objects.all()
        paginator = self.pagination_class()
        paginated_albums = paginator.paginate_queryset(albums, request)

        serializer = AlbumSerializers(paginated_albums, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = AlbumSerializers(data=request.data)
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
