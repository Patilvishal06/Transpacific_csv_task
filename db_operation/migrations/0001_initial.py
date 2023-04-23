# Generated by Django 3.2.18 on 2023-04-23 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('mobile_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('Status', models.CharField(default='active', max_length=20)),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
    ]
