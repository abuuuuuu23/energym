# Generated by Django 4.2.2 on 2023-09-08 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym1', '0002_rename_user_accounts_user_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='district',
            field=models.CharField(default=11, max_length=30),
            preserve_default=False,
        ),
    ]
