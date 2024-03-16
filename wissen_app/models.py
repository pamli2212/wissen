from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    domain = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class Project(models.Model):
    projectName = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    users = models.ManyToManyField(User)
    
    def __str__(self):
        return self.projectName





