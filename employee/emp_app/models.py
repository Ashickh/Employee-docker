from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=10, unique=True)
    designation = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
