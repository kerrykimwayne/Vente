# Generated by Django 4.2.2 on 2023-08-05 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Libele', models.CharField(max_length=50)),
                ('Date_Ajout', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-Date_Ajout'],
            },
        ),
        migrations.CreateModel(
            name='pagne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Libele', models.CharField(max_length=50)),
                ('prix', models.IntegerField()),
                ('Date_Ajout', models.DateTimeField(auto_now=True)),
                ('Categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='pagne.categorie')),
            ],
        ),
    ]
