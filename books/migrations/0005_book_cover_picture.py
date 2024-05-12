# Generated by Django 4.0 on 2024-05-12 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_remove_book_cover_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_picture',
            field=models.ImageField(default='cover_pictures/default.jpg', upload_to='cover_pictures'),
        ),
    ]