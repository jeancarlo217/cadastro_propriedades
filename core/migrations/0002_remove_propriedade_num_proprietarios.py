# Generated by Django 5.1.3 on 2024-11-13 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propriedade',
            name='num_proprietarios',
        ),
    ]
