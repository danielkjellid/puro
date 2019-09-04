# Generated by Django 2.1.5 on 2019-08-27 18:43

from django.db import migrations, models
import django.utils.timezone
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=255, verbose_name='fornavn')),
                ('last_name', models.CharField(max_length=255, verbose_name='etternavn')),
                ('birth_date', models.DateField(verbose_name='fødselsdag')),
                ('phone_number', phone_field.models.PhoneField(max_length=31)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='e-post')),
                ('has_confirmed_email', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=255, verbose_name='adresse')),
                ('zip_code', models.CharField(max_length=255, verbose_name='postkode')),
                ('zip_place', models.CharField(max_length=255, verbose_name='poststed')),
                ('disabled_emails', models.BooleanField(default=False)),
                ('subscribed_to_newsletter', models.BooleanField(default=True)),
                ('allow_personalization', models.BooleanField(default=True)),
                ('allow_third_party_personalization', models.BooleanField(default=True)),
                ('acquisition_source', models.CharField(blank=True, max_length=255, verbose_name='Opprettet gjennom')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_joined')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('roles', models.ManyToManyField(blank=True, related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='roles')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]