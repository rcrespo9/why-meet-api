# Generated by Django 3.1.6 on 2021-02-17 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_finalstep'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='is_final',
        ),
        migrations.RemoveField(
            model_name='step',
            name='is_go_to_meeting',
        ),
    ]
