from django.db import models
import uuid


    

class Criticy(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.UUID,editable=False,verbose_name="Criticy ID")
    level = models.CharField(max_length=50)

class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    criticy = models.OneToOneField(Criticy,verbose_name="Ticket Criticy")
    def __str__(self) -> str:
        return self.title

class Speciality(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.UUID,editable=False,verbose_name="Speciality ID")
    name = models.CharField(max_length=50,verbose_name="Speciality Name")

class Tech(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.UUID,editable=False,verbose_name="Tech ID")
    name = models.CharField(max_length=50,verbose_name="Tech Name")
    last_name = models.CharField(max_length=50,verbose_name="Tech Last_Name")
    speciality = models.ManyToManyField(Speciality, verbose_name="Speciality Name",blank=True,null=True)

class Ticket_History(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.UUID,editable=False,verbose_name="Ticket History ID")
    date = models.DateField(auto_now_add=True)
    description = models.TextField(verbose_name="Ticket History")
