# Generated by Django 4.0 on 2022-06-16 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_answernotification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentnotification',
            name='comment',
        ),
        migrations.DeleteModel(
            name='AnswerNotification',
        ),
        migrations.DeleteModel(
            name='CommentNotification',
        ),
    ]