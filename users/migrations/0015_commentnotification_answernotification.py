# Generated by Django 4.0 on 2022-06-16 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_rename_user_answer_author_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0014_remove_commentnotification_comment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_notifications', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forum.answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_notifications', to='auth.user')),
            ],
        ),
    ]
