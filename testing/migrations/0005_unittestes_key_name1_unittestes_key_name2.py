# Generated by Django 4.2.3 on 2023-07-21 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0004_alter_unittestes_json_alter_unittestes_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='unittestes',
            name='key_name1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='unittestes',
            name='key_name2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
