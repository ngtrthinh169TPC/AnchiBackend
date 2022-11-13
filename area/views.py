from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Area
from .serializers import AreaSerializer


class AreaAPI(APIView):
    def post(self, request):
        serializer = AreaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        area = serializer.save()
        return Response(status=201, data=serializer.data)


class AllAreasAPI(APIView):
    def get(self, request):
        areas = Area.objects.filter(verified=True)
        serializer = AreaSerializer(areas, many=True)
        return Response(status=200, data=serializer.data)
