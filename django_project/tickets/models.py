import uuid
from django.db import models
from users.models import User

class Ticket(models.Model):
    status_choices = (
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Pending', 'Pending')
    )
    ticket_no = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    date_created = models.DateTimeField(auto_now_add=True) 
    assigned_to = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    is_resolved = models.BooleanField(default=False)
    date_accepted = models.DateTimeField(null=True, blank=True)
    date_closed = models.DateTimeField(null=True, blank=True)
    ticket_status = models.CharField(max_length=15, choices=status_choices)


    class Meta:
        db_table = 'tickets'


    def __str__(self):
        return self.title