# Generated by Django 4.0.4 on 2022-05-17 11:28

from django.db import migrations

from openwisp_monitoring.device.migrations import assign_permissions_to_groups


class Migration(migrations.Migration):

    dependencies = [
        ('sample_device_monitoring', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            assign_permissions_to_groups, reverse_code=migrations.RunPython.noop
        ),
    ]
