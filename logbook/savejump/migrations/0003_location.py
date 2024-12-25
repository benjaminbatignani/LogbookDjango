# Generated by Django 5.1.4 on 2024-12-21 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savejump', '0002_altitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'location',
                'managed': True,
            },
        ),
    ]
