# Generated by Django 4.0 on 2021-12-13 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dogs',
            old_name='owner_id',
            new_name='owner',
        ),
    ]
