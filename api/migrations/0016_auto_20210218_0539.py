# Generated by Django 3.1.6 on 2021-02-18 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20210217_0756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firststep',
            name='step',
        ),
        migrations.AddField(
            model_name='step',
            name='is_first_step',
            field=models.BooleanField(default=False),
        ),
        migrations.AddConstraint(
            model_name='step',
            constraint=models.UniqueConstraint(condition=models.Q(is_first_step=True), fields=('is_first_step',), name='one_first_step'),
        ),
        migrations.DeleteModel(
            name='FirstStep',
        ),
    ]