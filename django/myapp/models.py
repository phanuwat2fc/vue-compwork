from django.db import models


# Create your models here.

class Events(models.Model):
    event = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.event


class Rank(models.Model):
    rank = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.rank

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255,null=True,blank=True)
    lastname = models.CharField(max_length=255,null=True,blank=True)
    rank = models.ForeignKey(Rank,null=True,blank=True,on_delete=models.CASCADE)
    event = models.ManyToManyField(Events,blank=True)
    phone = models.CharField(max_length=10,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.firstname




