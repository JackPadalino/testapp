# Generated by Django 4.0 on 2022-06-15 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
        ('users', '0002_profile_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='classes',
            field=models.ManyToManyField(blank=True, default=None, related_name='profiles', to='classroom.Classroom'),
        ),
    ]
