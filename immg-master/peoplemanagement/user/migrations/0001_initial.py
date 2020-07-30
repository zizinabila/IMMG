# Generated by Django 2.2.5 on 2019-09-29 15:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ktp_address', models.TextField(null=True)),
                ('current_address', models.TextField(null=True)),
                ('class_of', models.IntegerField(choices=[(1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)], null=True, validators=[django.core.validators.MinValueValidator(1991), user.models.max_value_current_year])),
                ('birth_date', models.DateField(default=django.utils.timezone.now)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.City')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.Country')),
                ('major', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.Major')),
                ('province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.Province')),
                ('tribe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.Tribe')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]