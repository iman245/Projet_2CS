# Generated by Django 5.0.3 on 2024-03-27 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0006_partenaire_labo'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratoire',
            name='Partenaire',
            field=models.ManyToManyField(related_name='Labo_chercheur', to='publication.partenaire_labo'),
        ),
    ]