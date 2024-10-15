from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255, null=True, blank=True)
    work = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {str(self.age)} {str(self.address)} {str(self.work)}'
