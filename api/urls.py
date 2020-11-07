from django.urls import path, include
from .router import api_urlpatterns as api_v1

app_name = 'api'

urlpatterns = [
    path('v1/', include(api_v1)),
]