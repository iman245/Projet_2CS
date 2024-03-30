# Generated by Django 5.0.3 on 2024-03-28 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0015_projet_themes'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='is_adminstrateur',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='is_chercheur',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='is_directeur_relex',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='is_editeur',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='is_responsable_fablab',
            field=models.BooleanField(default=False),
        ),
    ]