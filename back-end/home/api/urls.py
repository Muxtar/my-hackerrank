from django.urls import path
from .views import Api, test_api

urlpatterns = [
    path('', Api.as_view(), name = 'test_api'),
    path('test/', test_api)
]