# Generated by Django 3.0.5 on 2020-06-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0003_user_time_zone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityperiod',
            name='user_id',
        ),
        migrations.AddField(
            model_name='activityperiod',
            name='mydata',
            field=models.DateTimeField(null=True),
        ),
    ]
