# Generated by Django 2.2.1 on 2019-05-18 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estatebusiness', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='user',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='contract agent '),
        ),
    ]
