# Generated by Django 3.0.5 on 2021-02-22 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v0', '0008_auto_20210222_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
