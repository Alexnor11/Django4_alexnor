# Generated by Django 4.2.1 on 2024-10-23 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('develops', '0007_uploadfiles_alter_alexnor_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alexnor',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
