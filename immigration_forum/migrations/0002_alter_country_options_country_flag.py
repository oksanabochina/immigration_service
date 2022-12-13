# Generated by Django 4.1.3 on 2022-11-13 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immigration_forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AddField(
            model_name='country',
            name='flag',
            field=models.ImageField(blank=True, null=True, upload_to='images/country/'),
        ),
    ]
