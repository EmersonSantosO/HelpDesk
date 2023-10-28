from django.urls import path
from . import views

urlpatterns = [
    # URLs para Tickets
    path('tickets/', views.TicketListView.as_view(), name='ticket_list'),
    path('tickets/create/', views.TicketCreateView.as_view(), name='ticket_create'),
    path('tickets/<int:pk>/', views.TicketDetailView.as_view(), name='ticket_detail'),
    path('tickets/<int:pk>/edit/', views.TicketUpdateView.as_view(), name='ticket_update'),
    path('tickets/<int:pk>/delete/', views.TicketDeleteView.as_view(), name='ticket_delete'),

    # URLs para Ticket_History
    path('ticket-history/', views.TicketHistoryListView.as_view(), name='ticket_history_list'),
    path('ticket-history/create/', views.TicketHistoryCreateView.as_view(), name='ticket_history_create'),
    path('ticket-history/<int:pk>/', views.TicketHistoryDetailView.as_view(), name='ticket_history_detail'),
    path('ticket-history/<int:pk>/edit/', views.TicketHistoryUpdateView.as_view(), name='ticket_history_update'),
    path('ticket-history/<int:pk>/delete/', views.TicketHistoryDeleteView.as_view(), name='ticket_history_delete'),

    # URLs para Tech
    path('techs/', views.TechListView.as_view(), name='tech_list'),
    path('techs/create/', views.TechCreateView.as_view(), name='tech_create'),
    path('techs/<int:pk>/', views.TechDetailView.as_view(), name='tech_detail'),
    path('techs/<int:pk>/edit/', views.TechUpdateView.as_view(), name='tech_update'),
    path('techs/<int:pk>/delete/', views.TechDeleteView.as_view(), name='tech_delete'),

    # URLs para Speciality
    path('specialities/', views.SpecialityListView.as_view(), name='speciality_list'),
    path('specialities/create/', views.SpecialityCreateView.as_view(), name='speciality_create'),
    path('specialities/<int:pk>/', views.SpecialityDetailView.as_view(), name='speciality_detail'),
    path('specialities/<int:pk>/edit/', views.SpecialityUpdateView.as_view(), name='speciality_update'),
    path('specialities/<int:pk>/delete/', views.SpecialityDeleteView.as_view(), name='speciality_delete'),

    # URLs para Criticy
    path('criticities/', views.CriticyListView.as_view(), name='criticy_list'),
    path('criticities/create/', views.CriticyCreateView.as_view(), name='criticy_create'),
    path('criticities/<int:pk>/', views.CriticyDetailView.as_view(), name='criticy_detail'),
    path('criticities/<int:pk>/edit/', views.CriticyUpdateView.as_view(), name='criticy_update'),
    path('criticities/<int:pk>/delete/', views.CriticyDeleteView.as_view(), name='criticy_delete'),
]
