# Generated by Django 5.1.3 on 2024-11-13 20:30

import core.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('perfil', stdimage.models.StdImageField(blank=True, force_min_size=False, upload_to='perfil/', variations={'thumb': {'crop': True, 'height': 50, 'width': 50}})),
                ('tipo', models.CharField(choices=[('FUNC_V2', 'Funcionário V2'), ('FUNC_VV', 'Funcionário VV'), ('CLI_V2', 'Cliente V2'), ('DEV', 'Desenvolvimento')], default='DEV', max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('is_staff', models.BooleanField(default=True, verbose_name='Membros da Equipe')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', core.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CNPJ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=14, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('razao_social', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Propriedade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('matricula', models.CharField(max_length=100)),
                ('ccir', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15)),
                ('num_proprietarios', models.IntegerField()),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('titular', 'Titular'), ('cnpj', 'CNPJ')], max_length=10)),
                ('cnpj', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.cnpj')),
                ('representante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.proprietario')),
            ],
        ),
        migrations.CreateModel(
            name='ProprietarioPropriedade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propriedade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.propriedade')),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.proprietario')),
            ],
        ),
        migrations.CreateModel(
            name='Titular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('rg', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=255)),
                ('nacionalidade', models.CharField(max_length=100)),
                ('naturalidade', models.CharField(max_length=100)),
                ('estado_civil', models.CharField(max_length=50)),
                ('data_nascimento', models.DateField()),
                ('endereco', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.municipio')),
            ],
        ),
        migrations.AddField(
            model_name='proprietario',
            name='cpf',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.titular'),
        ),
    ]
