# Generated by Django 4.2 on 2024-05-28 18:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_cover_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookreview',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
