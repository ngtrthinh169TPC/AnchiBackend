from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tag
from .serializers import TagSerializer


class AllTagsAPI(APIView):
    def get(self, request):
        tags = Tag.objects.filter(verified=True)
        serializer = TagSerializer(tags, many=True)
        return Response(status=200, data=serializer.data)
