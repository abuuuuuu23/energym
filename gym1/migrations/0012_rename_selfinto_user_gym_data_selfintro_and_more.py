# Generated by Django 4.2.2 on 2023-09-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym1', '0011_rename_catagory_packages_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_gym_data',
            old_name='selfinto',
            new_name='selfintro',
        ),
        migrations.AlterField(
            model_name='packages',
            name='photo',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user_gym_data',
            name='height',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user_gym_data',
            name='joining_date',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user_gym_data',
            name='photo',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user_gym_data',
            name='start_date',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user_gym_data',
            name='weight',
            field=models.CharField(max_length=30),
        ),
    ]