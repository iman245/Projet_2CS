# Generated by Django 5.0.3 on 2024-03-26 23:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
                ('family_name', models.CharField(blank=True, max_length=254, null=True)),
                ('first_name', models.CharField(blank=True, max_length=254, null=True)),
                ('type', models.CharField(blank=True, max_length=254)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Demande_Partenariat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('etat', models.CharField(max_length=50)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Devis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etat', models.CharField(default='en attente', max_length=50)),
                ('montant', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipe_Projet',
            fields=[
                ('id_equipe_projet', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Equipe_Recherche',
            fields=[
                ('id_equipe_recherche', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id_formation', models.IntegerField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=50)),
                ('prix', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partenaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id_publication', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='publications/')),
                ('etat', models.CharField(max_length=50)),
                ('type_publication', models.CharField(max_length=50)),
                ('date_debut', models.DateTimeField(blank=True, null=True)),
                ('date_fin', models.DateTimeField(blank=True, null=True)),
                ('date_publication', models.DateTimeField(blank=True, null=True)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Chercheur',
            fields=[
                ('utilisateur_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('publication.utilisateur',),
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id_projet', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('equipe_projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publication.equipe_projet')),
            ],
        ),
        migrations.CreateModel(
            name='Theme_Recherche',
            fields=[
                ('id_theme', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('Equipe_Recherche', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publication.equipe_recherche')),
            ],
        ),
        migrations.CreateModel(
            name='Laboratoire',
            fields=[
                ('id_laboratoire', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('Partenaire', models.ManyToManyField(related_name='Labo_chercheur', to='publication.partenaire')),
                ('Chercheur', models.ManyToManyField(related_name='Labo_chercheur', to='publication.chercheur')),
            ],
        ),
        migrations.AddField(
            model_name='equipe_projet',
            name='Chercheur',
            field=models.ManyToManyField(related_name='equipes_projet', to='publication.chercheur'),
        ),
    ]
