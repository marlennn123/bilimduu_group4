from django.db import models


class Car(models.Model):
    category = models.CharField(max_length=64)
    marka = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    price = models.PositiveIntegerField(default=0)
    year = models.PositiveSmallIntegerField(default=0)
    mileage = models.PositiveIntegerField(default=0)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    with_photo = models.BooleanField(default=True)
    color = models.CharField(max_length=64)
    volume = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.marka


class Bet(models.Model):
    number = models.PositiveIntegerField(default=0)
    total_number = models.PositiveIntegerField(default=0)
    buy_now = models.PositiveIntegerField(default=0)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.number

#
# crud
# allauth(username, first_name, last_name, age, country, email, password) + google + github
# filter
# search
# order
# permissions

