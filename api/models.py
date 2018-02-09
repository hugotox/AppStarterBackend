from django.db import models


class Owner(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.TextField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
