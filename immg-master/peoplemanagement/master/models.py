from django.db import models
from django.contrib.auth.models import User
#Standard Model
# class Role(models.Model):
#     role_code = models.CharField(max_length=20)
#     role_desc = models.CharField(max_length=50)

#     def __str__(self):
#         return self.role_desc



class Gender(models.Model):
    gender_desc = models.CharField(max_length=50)

    def __str__(self):
        return u'{0}'.format(self.gender_desc)

class Country(models.Model):
    country_code = models.CharField(max_length=20)
    country_desc = models.CharField(max_length=50)

    def __str__(self):
        return u'{0}'.format(self.country_desc)

class Province(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    province_code = models.CharField(max_length=20)
    province_desc = models.CharField(max_length=50)

    def __str__(self):
        return u'{0}'.format(self.province_desc)

class City(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    city_code = models.CharField(max_length=20)
    city_desc = models.CharField(max_length=50)

    def __str__(self):
        return u'{0}'.format(self.city_desc)

#Custom Model
class Tribe(models.Model):
    tribe_code = models.CharField(max_length=20)
    tribe_desc = models.CharField(max_length=50)

    def __str__(self):
        return u'{0}'.format(self.tribe_desc)

class Major(models.Model):
    major_code = models.CharField(max_length=20)
    major_desc = models.CharField(max_length=50)

    def __str__(self):
        return u'{0}'.format(self.major_desc)

class Organization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    report_to = models.PositiveIntegerField()

    def __Str__(self):
        return u'{0}'.format(self.id)