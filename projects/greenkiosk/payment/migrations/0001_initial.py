# Generated by Django 4.2.1 on 2023-06-20 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date', models.DateTimeField()),
                ('payment_method', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
                ('currency', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
    ]