# Generated by Django 5.0.3 on 2024-04-01 15:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFablab', '0002_usersavedpiece'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demandemateriel',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='fablabinscriptionutilisateur',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='demandemateriel',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='fablabinscriptionutilisateur',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]