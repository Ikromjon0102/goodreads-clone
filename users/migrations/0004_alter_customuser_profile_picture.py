# Generated by Django 4.0 on 2024-05-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='default_profile_pictures.png', upload_to='profile_pictures'),
        ),
    ]
