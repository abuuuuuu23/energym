# Generated by Django 4.2.2 on 2023-09-29 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym1', '0007_rename_usergymdata_usergym_data'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='usergym_data',
            new_name='user_gymdata',
        ),
    ]
