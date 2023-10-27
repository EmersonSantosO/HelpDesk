from django.db import models
import uuid


    
#Es para darle que nivel de urgencia de atencion debe tener cada ticket
class Criticy(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.UUID,editable=False,verbose_name="Criticy ID")
    level = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.level



class Speciality(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.UUID,editable=False,verbose_name="Speciality ID")
    name = models.CharField(max_length=50,verbose_name="Speciality Name")

    def __str__(self) -> str:
        return self.name

class Tech(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.UUID,editable=False,verbose_name="Tech ID")
    name = models.CharField(max_length=50,verbose_name="Tech Name")
    last_name = models.CharField(max_length=50,verbose_name="Tech Last_Name")
    speciality = models.ManyToManyField(Speciality, verbose_name="Speciality Name",blank=True,null=True)

    def __str__(self) -> str:
        return self.name



class Ticket_History(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.UUID,editable=False,verbose_name="Ticket History ID")
    date = models.DateField(auto_now=True,verbose_name="Ticket Update")
    description = models.TextField(verbose_name="Description")

    def __str__(self) -> str:
        return self.date


class Ticket(models.Model):
    title = models.CharField(max_length=200,verbose_name="Ticket Title")
    description = models.TextField(verbose_name="Ticket Description")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Ticket Published")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Ticket Updated")
    criticy = models.OneToOneField(Criticy,verbose_name="Ticket Criticy",blank=True,null=True)
    tech = models.OneToOneField(Tech,verbose_name="Tech",blank=True,null=True)
    history = models.OneToOneField(Ticket_History,verbose_name="Ticket History",blank=True,null=True)    

    def __str__(self) -> str:
        return self.title