from django.contrib import admin
from .models import Ticket, Ticket_History, Tech, Speciality, Criticy

class TicketAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class TicketHistoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class TechAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class SpecialityAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class CriticyAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Ticket)
admin.site.register(Ticket_History)
admin.site.register(Tech)
admin.site.register(Speciality)
admin.site.register(Criticy)
