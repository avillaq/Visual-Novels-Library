# Generated by Django 5.0.2 on 2025-01-20 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VNDisplay', '0012_rename_image_url_post_cover_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publicaction_date',
            new_name='publication_date',
        ),
    ]
