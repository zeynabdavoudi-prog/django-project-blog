# Generated by Django 5.1 on 2024-08-28 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/feature-img2.jpg', upload_to='blog/'),
        ),
    ]
