# Generated by Django 3.0.5 on 2020-06-21 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0004_auto_20200621_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activityperiod',
            old_name='mydata',
            new_name='end_time',
        ),
        migrations.AddField(
            model_name='activityperiod',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
