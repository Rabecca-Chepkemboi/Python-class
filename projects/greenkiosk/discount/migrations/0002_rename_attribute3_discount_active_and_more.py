# Generated by Django 4.2.1 on 2023-06-30 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='attribute3',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='discount',
            old_name='attribute4',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='discount',
            old_name='attribute2',
            new_name='items_bought',
        ),
        migrations.RenameField(
            model_name='discount',
            old_name='attribute1',
            new_name='name',
        ),
    ]
