from django.db import models


class Token(models.Model):
    YOUTUBE = 'YT'
    SPOTIFY = 'SF'
    MEDIA_TYPE_CHOICES = (
        (YOUTUBE, 'YouTube'),
        (SPOTIFY, 'Spotify'),
    )
    CHICKEN = 'CK'
    CAT = 'CT'
    DOG = 'DG'
    HORSE = 'HS'
    ELEPHANT = 'EL'
    TOKEN_TYPE_CHOICES = (
        (CHICKEN, 'Chicken'),
        (CAT, 'Cat'),
        (DOG, 'Dog'),
        (HORSE, 'Horse'),
        (ELEPHANT, 'Elephant'),
    )
    token_type = models.CharField(max_length=2, choices=TOKEN_TYPE_CHOICES,
                                  default=CHICKEN)
    media_type = models.CharField(
        max_length=2,
        choices=MEDIA_TYPE_CHOICES,
        default=YOUTUBE)
    duration = models.IntegerField(null=False, default=0)
    is_active = models.BooleanField(default=True)


class Accounting(models.Model):
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

    limits = models.IntegerField(null=False, default=0)
