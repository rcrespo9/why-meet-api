# Generated by Django 3.1.6 on 2021-03-05 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20210219_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='text',
            field=models.TextField(unique=True),
        ),
    ]
