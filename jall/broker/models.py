from django.db import models


class Token(models.Model):
    YOUTUBE = 'YT'
    SPOTIFY = 'SF'
    MEDIA_TYPE_CHOICES = (
        (YOUTUBE, 'YouTube'),
        (SPOTIFY, 'Spotify'),
    )
    media_type = models.CharField(
        max_length=2,
        choices=MEDIA_TYPE_CHOICES,
        default=YOUTUBE)
    duration = models.IntegerField(null=False)
    is_active = models.BooleanField(default=True)
