from django.urls import path
from .views import ImageCompressView

urlpatterns = [
    path('compress/', ImageCompressView.as_view(), name='compress'),
]