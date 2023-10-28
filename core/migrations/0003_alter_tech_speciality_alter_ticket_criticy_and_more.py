# Generated by Django 4.2.6 on 2023-10-28 01:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_criticy_speciality_ticket_history_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tech',
            name='speciality',
            field=models.ManyToManyField(blank=True, to='core.speciality', verbose_name='Speciality Name'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='criticy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.criticy', verbose_name='Ticket Criticy'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='history',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.ticket_history', verbose_name='Ticket History'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='id',
            field=models.UUIDField(default=uuid.UUID, editable=False, primary_key=True, serialize=False, verbose_name='Ticket ID'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='tech',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.tech', verbose_name='Tech'),
        ),
    ]
