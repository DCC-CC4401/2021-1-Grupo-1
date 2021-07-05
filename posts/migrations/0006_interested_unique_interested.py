# Generated by Django 3.2 on 2021-07-03 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_interested_date'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='interested',
            constraint=models.UniqueConstraint(fields=('user', 'post'), name='unique_interested'),
        ),
    ]