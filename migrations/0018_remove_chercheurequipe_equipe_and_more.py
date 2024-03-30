# Generated by Django 5.0.3 on 2024-03-28 09:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0017_delete_chercheur_chercheur_chercheurequipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chercheurequipe',
            name='equipe',
        ),
        migrations.RemoveField(
            model_name='chercheurequipe',
            name='utilisateur_ptr',
        ),
        migrations.DeleteModel(
            name='Chercheur',
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='equipeRecherche',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chercheurs', to='publication.equipe_recherche'),
        ),
        migrations.AlterField(
            model_name='equipe_projet',
            name='Chercheur',
            field=models.ManyToManyField(related_name='equipe_projet', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='equipe_projet',
            name='id_equipe_projet',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='equipe_recherche',
            name='id_equipe_recherche',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='ChercheurEquipe',
        ),
    ]