from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=250)
    source = models.CharField(max_length=100)
    date = models.DateField()
    url = models.URLField()
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)

    def __str__(self):
        return self.title
