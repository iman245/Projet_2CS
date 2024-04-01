# Generated by Django 5.0.3 on 2024-03-30 13:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0002_alter_laboratoire_id_laboratoire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id_club', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('slogan', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='club/')),
            ],
        ),
        migrations.AddField(
            model_name='publication',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='publication.club'),
        ),
        migrations.CreateModel(
            name='MembreClub',
            fields=[
                ('id_membre', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('post', models.TextField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membres', to='publication.club')),
            ],
        ),
    ]
