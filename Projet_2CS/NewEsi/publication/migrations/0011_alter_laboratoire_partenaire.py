# Generated by Django 5.0.3 on 2024-03-27 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0010_laboratoire_partenaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratoire',
            name='Partenaire',
            field=models.ManyToManyField(related_name='Labo_partner', to='publication.partenaire_labo'),
        ),
    ]
