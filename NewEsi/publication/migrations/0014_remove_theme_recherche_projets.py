# Generated by Django 5.0.3 on 2024-03-28 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0013_partenaire_labo_laboratoire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme_recherche',
            name='projets',
        ),
    ]
