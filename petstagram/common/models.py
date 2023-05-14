from django.db import models

from petstagram.photos.models import Photo


# Create your models here.
class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateField(
        auto_now=True,
    )
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )

    class Mete:
        ordering = ["-date_time_of_publication"]


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE
    )
