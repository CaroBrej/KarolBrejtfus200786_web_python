from django.db import models

# Create your models here.


class SportClub(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=200)
    organizator = models.ForeignKey(SportClub, on_delete=models.SET_NULL, null=True, blank=True)
    rank = models.CharField(max_length=100)
    rank_point = models.IntegerField(default=1)
    year = models.CharField(max_length=10)

    def __str__(self):
        return self.name + " " + self.year


class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    sport_club = models.ForeignKey(SportClub, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    born_year = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Person name: " + self.name + " surname: " + self.surname


class Results(models.Model):
    place = models.IntegerField()
    participant = models.ForeignKey(Person, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    category_age = models.CharField(max_length=100)
    category_weight = models.CharField(max_length=20)

    def __str__(self):
        return self.participant.name + " " + self.participant.surname + " " + str(self.place)
