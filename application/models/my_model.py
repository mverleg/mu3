
from django.db import models


class MyModel(models.Model):
    
    name = models.CharField(max_length = 32)
    
    class Meta:
        app_label = 'appname'


