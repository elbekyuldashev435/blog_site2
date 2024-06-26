# Generated by Django 5.0.4 on 2024-06-01 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='all/image'),
        ),
        migrations.AlterField(
            model_name='products',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='all/video'),
        ),
    ]
