# Generated by Django 5.0.1 on 2024-01-22 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(default=1, upload_to='post'),
            preserve_default=False,
        ),
    ]