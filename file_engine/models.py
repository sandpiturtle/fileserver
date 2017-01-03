from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    # The files will be automatically uploaded to MEDIA_ROOT/documents/
    document = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
