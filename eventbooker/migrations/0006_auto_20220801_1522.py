# Generated by Django 3.2.14 on 2022-08-01 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventbooker', '0005_auto_20220801_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='timeslots',
        ),
        migrations.AddField(
            model_name='timeslot',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='associated_event', to='eventbooker.event'),
        ),
    ]