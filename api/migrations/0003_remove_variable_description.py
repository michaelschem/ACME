# Generated by Django 3.1.4 on 2020-12-20 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_variable_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variable',
            name='description',
        ),
    ]