# Generated by Django 2.1.5 on 2019-09-12 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phone_field.models
#import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalUser',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=255, verbose_name='fornavn')),
                ('last_name', models.CharField(max_length=255, verbose_name='etternavn')),
                ('birth_date', models.DateField(verbose_name='fødselsdag')),
                ('phone_number', phone_field.models.PhoneField(max_length=31)),
                ('email', models.EmailField(db_index=True, max_length=255, verbose_name='e-post')),
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
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical user',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            #bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
