# File: models.py
# Author: Justin Wang (justin1@bu.edu), 4/3/2025
# Description: Models

from django.db import models

# Create your models here.

class Voter(models.Model):
    '''Voter model representing voter registration and voting history data'''
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    residential_street_number = models.CharField(max_length=20)
    residential_street_name = models.CharField(max_length=200)
    residential_apartment_number = models.CharField(max_length=20, blank=True)
    residential_zip_code = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    date_of_registration = models.DateField()
    party_affiliation = models.CharField(max_length=10)
    precinct_number = models.CharField(max_length=10)
    v20state = models.CharField(max_length=5)
    v21town = models.CharField(max_length=5)
    v21primary = models.CharField(max_length=5)
    v22general = models.CharField(max_length=5)
    v23town = models.CharField(max_length=5)
    voter_score = models.IntegerField()

    def __str__(self):
        '''Return a string representation of this model instance.'''
        return f"{self.first_name} {self.last_name}"


def load_data():
    '''Function to load data records from CSV file into Django model instances.'''

    Voter.objects.all().delete()

    filename = '/Users/justin/Downloads/newton_voters.csv'
    f = open(filename)
    f.readline()

    for line in f:
        fields = line.split(',')

        try:
            voter = Voter(
                last_name = fields[1],
                first_name = fields[2],
                residential_street_number = fields[3],
                residential_street_name = fields[4],
                residential_apartment_number = fields[5],
                residential_zip_code = fields[6],
                date_of_birth = fields[7],
                date_of_registration = fields[8],
                party_affiliation = fields[9].strip(),
                precinct_number = fields[10],
                v20state = fields[11],
                v21town = fields[12],
                v21primary = fields[13],
                v22general = fields[14],
                v23town = fields[15],
                voter_score = fields[16]
            )
            voter.save()
        except Exception as e:
            print(f'Error: {e}')
    f.close()