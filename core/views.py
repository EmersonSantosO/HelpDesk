from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Ticket
from .forms import TicketForm
class TicketListView(ListView):
    model = Ticket
    template_name = "ticket_list.html"
    context_object_name = "tickets"

class TicketDetailView(DetailView):
    model = Ticket
    template_name = "ticket_detail.html"
    context_object_name = "ticket"

class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = "ticket_form.html"
    success_url = reverse_lazy("ticket_list")

class TicketUpdateView(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = "ticket_form.html"
    success_url = reverse_lazy("ticket_list")

class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = "ticket_confirm_delete.html"
    success_url = reverse_lazy("ticket_list")