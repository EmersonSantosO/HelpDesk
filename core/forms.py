from django import forms
from .models import Ticket, Ticket_History, Tech, Speciality, Criticy

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title","description","criticy","tech","history"]
        widgets = {"title":forms.TextInput(attrs={"class":"form-control"}),
                   "description":forms.Textarea(attrs={"class":"form-control"}),
                   "criticy":forms.Select(attrs={"class":"form-control"}),
                   "tech":forms.Select(attrs={"class":"form-control"}),
                   "history":forms.Select(attrs={"class":"form-control"}),
                   }

class Ticket_HistoryForm(forms.ModelForm):
    class Meta:
        model = Ticket_History
        fields = ["date","description"]
        widgets = {"date":forms.DateInput(attrs={"class":"form-control"}),
                   "description":forms.Textarea(attrs={"class":"form-control"}),
                   }

class TechForm(forms.ModelForm):
    class Meta:
        model = Tech
        fields = ["name","last_name","speciality"]
        widgets = {"name":forms.TextInput(attrs={"class":"form-control"}),
                   "last_name":forms.TextInput(attrs={"class":"form-control"}),
                   "speciality":forms.Select(attrs={"class":"form-control"}),
                   }

class SpecialityForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = ["name"]
        widgets = {"name":forms.TextInput(attrs={"class":"form-control"}),
                   }

class CriticyForm(forms.ModelForm):
    class Meta:
        model = Criticy
        fields = ["level"]
        widgets = {"level":forms.TextInput(attrs={"class":"form-control"}),
                   }

