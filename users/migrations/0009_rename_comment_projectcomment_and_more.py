# Generated by Django 4.0 on 2022-06-16 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0008_comment_commentnotification'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='ProjectComment',
        ),
        migrations.RenameModel(
            old_name='CommentNotification',
            new_name='ProjectCommentNotification',
        ),
    ]