# Generated by Django 5.1 on 2024-08-28 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_options_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='statics/img/feature-img1.png', upload_to='blog/'),
        ),
    ]
