# Generated by Django 3.0.1 on 2019-12-26 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('utils', '0002_delete_changelog'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('changes', models.TextField(blank=True, verbose_name='changes')),
                ('date_of_change', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='change time')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType', verbose_name='content type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='changed_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Change log entry',
                'verbose_name_plural': 'Change log entries',
            },
        ),
    ]
