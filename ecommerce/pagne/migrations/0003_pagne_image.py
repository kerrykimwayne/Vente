# Generated by Django 4.2.2 on 2023-08-06 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagne', '0002_alter_pagne_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagne',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img_update'),
        ),
    ]