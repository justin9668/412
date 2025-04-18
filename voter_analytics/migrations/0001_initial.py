# Generated by Django 5.1.5 on 2025-04-04 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('residential_street_number', models.CharField(max_length=20)),
                ('residential_street_name', models.CharField(max_length=200)),
                ('residential_apartment_number', models.CharField(blank=True, max_length=20)),
                ('residential_zip_code', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('date_of_registration', models.DateField()),
                ('party_affiliation', models.CharField(max_length=10)),
                ('precinct_number', models.CharField(max_length=10)),
                ('v20state', models.CharField(max_length=5)),
                ('v21town', models.CharField(max_length=5)),
                ('v21primary', models.CharField(max_length=5)),
                ('v22general', models.CharField(max_length=5)),
                ('v23town', models.CharField(max_length=5)),
                ('voter_score', models.IntegerField()),
            ],
        ),
    ]
