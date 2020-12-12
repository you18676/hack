from django.db import models


class Memo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    pub_date = models.DateTimeField('date published', null=True, blank=True)
