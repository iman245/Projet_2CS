# Generated by Django 5.0.3 on 2024-05-10 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0002_alter_theme_recherche_id_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='id_projet',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
