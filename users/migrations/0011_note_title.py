# Generated by Django 2.1.5 on 2019-12-11 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20190913_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(default='Tittel', max_length=255, verbose_name='Tittel'),
            preserve_default=False,
        ),
    ]