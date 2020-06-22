
from django.urls import path, include
from .views import NewsAPIView

urlpatterns = [
    path('', NewsAPIView.as_view(), name='api')
]

