# Generated by Django 3.0.5 on 2022-10-28 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='phone_number',
            new_name='number',
        ),
    ]
