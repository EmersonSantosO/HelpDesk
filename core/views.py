from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Ticket, Ticket_History, Tech, Speciality, Criticy
from .forms import TicketForm, Ticket_HistoryForm, TechForm, SpecialityForm, CriticyForm



# Vistas para Ticket
class TicketListView(ListView):
    model = Ticket
    template_name = 'ticket_list.html'

class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'ticket_detail.html'

class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket_form.html'
    success_url = reverse_lazy('ticket_list')

class TicketUpdateView(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket_form.html'
    success_url = reverse_lazy('ticket_list')

class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = 'ticket_confirm_delete.html'
    success_url = reverse_lazy('ticket_list')

# Vistas para Ticket_History
class TicketHistoryListView(ListView):
    model = Ticket_History
    template_name = 'ticket_history_list.html'

class TicketHistoryDetailView(DetailView):
    model = Ticket_History
    template_name = 'ticket_history_detail.html'

class TicketHistoryCreateView(CreateView):
    model = Ticket_History
    form_class = Ticket_HistoryForm
    template_name = 'ticket_history_form.html'
    success_url = reverse_lazy('history_list')

class TicketHistoryUpdateView(UpdateView):
    model = Ticket_History
    form_class = Ticket_HistoryForm
    template_name = 'ticket_history_form.html'
    success_url = reverse_lazy('history_list')

class TicketHistoryDeleteView(DeleteView):
    model = Ticket_History
    template_name = 'ticket_history_confirm_delete.html'
    success_url = reverse_lazy('history_list')

# Vistas para Tech
class TechListView(ListView):
    model = Tech
    template_name = 'tech_list.html'

class TechDetailView(DetailView):
    model = Tech
    template_name = 'tech_detail.html'

class TechCreateView(CreateView):
    model = Tech
    form_class = TechForm
    template_name = 'tech_form.html'
    success_url = reverse_lazy('tech_list')

class TechUpdateView(UpdateView):
    model = Tech
    form_class = TechForm
    template_name = 'tech_form.html'
    success_url = reverse_lazy('tech_list')

class TechDeleteView(DeleteView):
    model = Tech
    template_name = 'tech_confirm_delete.html'
    success_url = reverse_lazy('tech_list')

# Vistas para Speciality
class SpecialityListView(ListView):
    model = Speciality
    template_name = 'speciality_list.html'

class SpecialityDetailView(DetailView):
    model = Speciality
    template_name = 'speciality_detail.html'

class SpecialityCreateView(CreateView):
    model = Speciality
    form_class = SpecialityForm
    template_name = 'speciality_form.html'
    success_url = reverse_lazy('speciality_list')

class SpecialityUpdateView(UpdateView):
    model = Speciality
    form_class = SpecialityForm
    template_name = 'speciality_form.html'
    success_url = reverse_lazy('speciality_list')

class SpecialityDeleteView(DeleteView):
    model = Speciality
    template_name = 'speciality_confirm_delete.html'
    success_url = reverse_lazy('speciality_list')

# Vistas para Criticy
class CriticyListView(ListView):
    model = Criticy
    template_name = 'criticy_list.html'

class CriticyDetailView(DetailView):
    model = Criticy
    template_name = 'criticy_detail.html'

class CriticyCreateView(CreateView):
    model = Criticy
    form_class = CriticyForm
    template_name = 'criticy_form.html'
    success_url = reverse_lazy('criticy_list')

class CriticyUpdateView(UpdateView):
    model = Criticy
    form_class = CriticyForm
    template_name = 'criticy_form.html'
    success_url = reverse_lazy('criticy_list')

class CriticyDeleteView(DeleteView):
    model = Criticy
    template_name = 'criticy_confirm_delete.html'
    success_url = reverse_lazy('criticy_list')
