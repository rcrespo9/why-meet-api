# Generated by Django 3.1.6 on 2021-03-06 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20210306_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='children',
            field=models.ManyToManyField(through='api.Choice', to='api.Step'),
        ),
    ]
