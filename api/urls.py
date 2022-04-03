from django.urls import path
from api.views import RecordListCreateAPIView


app_name = "api"

urlpatterns = [
    path("post/", RecordListCreateAPIView.as_view(), name="create_list_post")
]
