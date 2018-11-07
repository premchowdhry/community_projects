from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

WORK_CHOICES = (
    ('tutoring', 'Tutoring'),
    ('wildlife_conservation', 'Wildlife Conservation'),
    ('construction', 'Construction'),
    ('ocean_cleaning', 'Ocean Cleaning'),
    ('street_cleaning', 'Street Cleaning'),
)


def get_image_path(instance, filename):
    return os.path.join('company_logo', str(instance.id), filename)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    title = models.CharField(max_length=100)
    # location = map_fields.AddressField(max_length=200)
    # geolocation = map_fields.GeoLocationField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')
    type = models.CharField(
        max_length=50, choices=WORK_CHOICES, default='tutoring')
    estimate_hours = models.IntegerField(
        default=1, validators=[MinValueValidator(1)])
    work_date = models.DateTimeField(default=timezone.now, blank=True)
    description = models.TextField(default='')
    company = models.CharField(max_length=100, default='')
    company_logo = models.ImageField(
        upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.title
