# Generated by Django 4.0 on 2022-06-16 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_projectnotification_delete_notification'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectNotification',
        ),
    ]