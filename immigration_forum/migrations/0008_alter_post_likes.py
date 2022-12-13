# Generated by Django 4.1.3 on 2022-12-07 16:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('immigration_forum', '0007_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
