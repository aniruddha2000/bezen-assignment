from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from api.models import Record
from api.serializers import RecordListCreateSerializer


class RecordCreateAPIView(ListCreateAPIView):
    queryset = Record.objects.order_by('timestamp')
    serializer_class = RecordListCreateSerializer

    # def perform_create(self, serializer):
    #     return serializer.save(auther=Record.objects.get(id=self.request.user.id))

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     instance = self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     serializer = PostListSerializer(instance=instance, many=False)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = PostListSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def get_queryset(self):
    #     queryset = FoodPost.objects.filter(
    #         auther=Record.objects.get(id=self.request.user.id))
    #     return queryset
