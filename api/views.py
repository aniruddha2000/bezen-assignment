from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from api.models import Record
from api.serializers import RecordListCreateSerializer


class RecordListCreateAPIView(ListCreateAPIView):
    queryset = Record.objects.order_by('-timestamp')
    serializer_class = RecordListCreateSerializer
