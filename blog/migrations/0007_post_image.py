# Generated by Django 5.0.6 on 2024-06-02 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_options_comment_createat_tags_createat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/default.jpg', upload_to='blog/%Y/%m/%d/'),
        ),
    ]
