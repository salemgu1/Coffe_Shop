# Generated by Django 3.0.5 on 2020-10-07 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0002_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='coffee_pic/'),
        ),
    ]
