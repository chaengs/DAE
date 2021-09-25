# Generated by Django 3.2.7 on 2021-09-25 07:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='applicant',
            field=models.ManyToManyField(blank=True, related_name='apply', to=settings.AUTH_USER_MODEL),
        ),
    ]
