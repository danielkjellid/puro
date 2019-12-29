# Generated by Django 3.0.1 on 2019-12-28 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_note_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'permissions': (('has_note_view', 'User can view notes'), ('has_note_add', 'User can add notes'), ('has_note_edit', 'User can edit notes'), ('has_note_delete', 'User can delete notes')), 'verbose_name': 'Note', 'verbose_name_plural': 'Notes'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('has_users_export', 'Can export users list'), ('has_users_access', 'Can list and search users'), ('has_user_add', 'Allows the user to add new users'), ('has_user_management', 'Can edit user details'), ('has_user_export', 'Can export user details'), ('has_user_hijack', 'Can log in as user'), ('has_user_high_level_management', 'Can toggle users active state')), 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]