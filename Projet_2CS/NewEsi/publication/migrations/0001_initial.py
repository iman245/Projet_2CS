# Generated by Django 5.0.3 on 2024-04-17 18:33

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
            name='Annuaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='annuaire_photos/')),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('mot_cle', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id_club', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('slogan', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='club/')),
            ],
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
            name='Equipe_Recherche',
            fields=[
                ('id_equipe_recherche', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('theme', models.CharField(default='', max_length=255)),
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
            name='Laboratoire',
            fields=[
                ('id_laboratoire', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
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
            name='Theme_Recherche',
            fields=[
                ('id_theme', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
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
                ('is_chercheur', models.BooleanField(default=False)),
                ('is_adminstrateur', models.BooleanField(default=False)),
                ('is_editeur', models.BooleanField(default=False)),
                ('is_responsable_fablab', models.BooleanField(default=False)),
                ('is_directeur_relex', models.BooleanField(default=False)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('equipeRecherche', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chercheurs', to='publication.equipe_recherche')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Administration_Annuaire',
            fields=[
                ('annuaire_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='publication.annuaire')),
                ('service', models.CharField(blank=True, max_length=100)),
            ],
            bases=('publication.annuaire',),
        ),
        migrations.CreateModel(
            name='Alumnie_Annuaire',
            fields=[
                ('annuaire_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='publication.annuaire')),
                ('promotion', models.IntegerField(blank=True)),
            ],
            bases=('publication.annuaire',),
        ),
        migrations.CreateModel(
            name='Enseignant_Annuaire',
            fields=[
                ('annuaire_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='publication.annuaire')),
                ('grade', models.CharField(blank=True, choices=[('professeur', 'Professeur'), ('maître de conférences A', 'Maître de conférences A'), ('maître de conférences B', 'Maître de conférences B')], max_length=50)),
            ],
            bases=('publication.annuaire',),
        ),
        migrations.AddField(
            model_name='equipe_recherche',
            name='laboratoire',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Equipe_recherche', to='publication.laboratoire'),
        ),
        migrations.CreateModel(
            name='Equipe_Projet',
            fields=[
                ('id_equipe_projet', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('Chercheur', models.ManyToManyField(related_name='equipe_projet', to=settings.AUTH_USER_MODEL)),
                ('laboratoire', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Equipes_projet', to='publication.laboratoire')),
            ],
        ),
        migrations.CreateModel(
            name='MembreClub',
            fields=[
                ('id_membre', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('post', models.TextField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membres', to='publication.club')),
            ],
        ),
        migrations.CreateModel(
            name='Partenaire_labo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('laboratoire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='publication.laboratoire')),
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
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='publication.club')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('titre', models.CharField(max_length=255)),
                ('contenu', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publication.question')),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id_projet', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('equipe_projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publication.equipe_projet')),
                ('themes', models.ManyToManyField(related_name='themes', to='publication.theme_recherche')),
            ],
        ),
    ]
