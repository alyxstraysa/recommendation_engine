# Generated by Django 3.1.4 on 2020-12-14 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime_app', '0002_delete_temp'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Anime',
            new_name='Anime_Pref',
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='Anime_User',
        ),
    ]