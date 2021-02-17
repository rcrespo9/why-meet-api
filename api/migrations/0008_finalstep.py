# Generated by Django 3.1.6 on 2021-02-16 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210216_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalStep',
            fields=[
                ('step', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='final_step', serialize=False, to='api.step')),
                ('is_go', models.BooleanField(default=False)),
            ],
        ),
    ]
