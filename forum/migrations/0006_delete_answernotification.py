# Generated by Django 4.0 on 2022-06-16 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_answernotification_delete_questionnotification'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnswerNotification',
        ),
    ]
