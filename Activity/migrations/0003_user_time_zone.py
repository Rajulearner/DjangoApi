# Generated by Django 3.0.5 on 2020-06-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0002_remove_user_timezone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='time_zone',
            field=models.CharField(default='india', max_length=40),
            preserve_default=False,
        ),
    ]
