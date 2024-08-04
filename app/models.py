from django.db import models

class Upload(models.Model):
    Image = models.ImageField(upload_to="image")
    description = models.TextField(max_length=500)

    class Meta:
        db_table = 'app_upload'
        verbose_name = 'upload'
        verbose_name_plural = 'uploades'
        ordering = ('-id',)

    def __str__(self):
        return self.Image
