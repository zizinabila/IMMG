from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator
from master.models import Country, Province, City, Tribe, Major, Gender
import datetime
from django.core.validators import RegexValidator

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)
    
def year_choices():
    return [(r,r) for r in range(1991, datetime.date.today().year+1)]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    tribe = models.ForeignKey(Tribe, on_delete=models.SET_NULL, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Phone number must be entered in the format: '+6281297126699' or 081297126699. Up to 14 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=14, null=True)
    ktp_address = models.TextField(null=True)
    current_address = models.TextField(null=True)
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True)
    class_of = models.IntegerField(choices=year_choices(), validators=[MinValueValidator(1991), max_value_current_year], null=True)
    birth_date = models.DateField(default=timezone.now)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        # super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
