# Generated by Django 4.0.4 on 2022-07-25 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_remove_post_featured_image_post_imagen_portada_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
