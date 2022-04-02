from rest_framework.serializers import ModelSerializer
from api.views import Record


class RecordListCreateSerializer(ModelSerializer):
    class Meta:
        model = Record
