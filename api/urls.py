from django.urls import path
from api.views import RecordCreateAPIView


app_name = "api"

urlpatterns = [
    path("post/", RecordCreateAPIView.as_view(), name="create_list_post")
]
