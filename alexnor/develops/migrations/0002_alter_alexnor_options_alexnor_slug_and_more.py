# Generated by Django 4.2.1 on 2024-10-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('develops', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alexnor',
            options={'ordering': ['-time_create']},
        ),
        migrations.AddField(
            model_name='alexnor',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AddIndex(
            model_name='alexnor',
            index=models.Index(fields=['-time_create'], name='develops_al_time_cr_c72507_idx'),
        ),
    ]
