# Generated by Django 4.1.7 on 2023-03-17 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_remove_tier_thumbnail_height_image_image_thumb_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_thumb_1',
            new_name='thumb_image_1',
        ),
        migrations.RenameField(
            model_name='tier',
            old_name='thumbnail_1_height',
            new_name='thumbnail_height',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_thumb_2',
        ),
        migrations.RemoveField(
            model_name='tier',
            name='thumbnail_2_height',
        ),
    ]
