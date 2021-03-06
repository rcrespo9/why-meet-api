# Generated by Django 3.1.6 on 2021-03-06 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20210305_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='is_interstitial',
        ),
        migrations.CreateModel(
            name='InterstitialStep',
            fields=[
                ('step', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='interstitial_step', serialize=False, to='api.step')),
                ('next_step', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.step')),
            ],
        ),
    ]