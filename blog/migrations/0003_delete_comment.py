# Generated by Django 5.0.6 on 2024-05-31 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_comments_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]