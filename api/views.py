from rest_framework import generics
from .models import News
from .serializers import NewsSerializer

# Create your views here.
class NewsAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
