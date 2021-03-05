# Generated by Django 3.1.6 on 2021-02-19 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20210218_0611'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='choice',
            constraint=models.UniqueConstraint(fields=('step', 'next_step'), name='unique_step_next_step'),
        ),
    ]