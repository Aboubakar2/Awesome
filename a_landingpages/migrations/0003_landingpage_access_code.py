# Generated by Django 5.0.6 on 2024-07-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_landingpages', '0002_rename_landinpage_landingpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='access_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
