# Generated by Django 5.0.3 on 2024-03-20 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theme_recherche',
            old_name='Equipe_Recherchee',
            new_name='Equipe_Recherche',
        ),
    ]