from django.db import models

from apps.accounts.models import User
from apps.events.models import Event


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="sold_tickets")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets")
    created_at = models.DateTimeField(auto_now_add=True)
