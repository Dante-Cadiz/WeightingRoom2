# Generated by Django 3.2.14 on 2022-08-07 11:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventbooker', '0011_auto_20220803_1030'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Timeslot',
            new_name='EventTimeslot',
        ),
    ]