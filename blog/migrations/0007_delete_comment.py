# Generated by Django 3.0.6 on 2020-05-18 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200518_1923'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
