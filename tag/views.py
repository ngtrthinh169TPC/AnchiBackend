from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tag
from .serializers import TagSerializer


class TagAPI(APIView):
    def post(self, request):
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tag = serializer.save()
        return Response(status=201, data=serializer.data)


class AllTagsAPI(APIView):
    def get(self, request):
        tags = Tag.objects.filter(verified=True)
        serializer = TagSerializer(tags, many=True)
        return Response(status=200, data=serializer.data)
