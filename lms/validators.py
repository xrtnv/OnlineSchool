from django.core.exceptions import ValidationError


def validate_youtube_url(field):
    if 'youtube.com' not in field:
        raise ValidationError('Ссылка должна вести только на youtube.com.')
