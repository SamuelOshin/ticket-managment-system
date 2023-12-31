# Generated by Django 4.2.1 on 2023-06-08 17:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_no', models.UUIDField(default=uuid.uuid4)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_resolved', models.BooleanField(default=False)),
                ('date_accepted', models.DateTimeField(blank=True, null=True)),
                ('date_closed', models.DateTimeField(blank=True, null=True)),
                ('ticket_status', models.CharField(choices=[('Active', 'Active'), ('Completed', 'Completed'), ('Pending', 'Pending')], max_length=15)),
            ],
        ),
    ]
