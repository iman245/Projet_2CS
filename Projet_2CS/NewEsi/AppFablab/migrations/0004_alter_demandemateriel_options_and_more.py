# Generated by Django 5.0.3 on 2024-04-01 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFablab', '0003_alter_demandemateriel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demandemateriel',
            options={'ordering': ['-date_emprunt']},
        ),
        migrations.RemoveField(
            model_name='demandemateriel',
            name='created',
        ),
        migrations.AlterField(
            model_name='fablabinscriptionutilisateur',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]