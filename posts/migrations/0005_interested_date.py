# Generated by Django 3.2 on 2021-07-02 22:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210702_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='interested',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
