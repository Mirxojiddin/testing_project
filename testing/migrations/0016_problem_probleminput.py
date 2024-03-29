# Generated by Django 5.0 on 2024-01-09 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0015_remove_unittestes_login_json_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.problem')),
            ],
        ),
    ]
