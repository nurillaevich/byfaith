# Generated by Django 5.0.1 on 2024-01-31 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=212)),
                ('des', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
