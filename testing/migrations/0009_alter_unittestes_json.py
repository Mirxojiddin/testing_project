# Generated by Django 4.2.3 on 2023-07-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0008_unittestes_param4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unittestes',
            name='json',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
