import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Ticket
from .form import CreateTicketForm, UpdateTicketForm
from .models import User
from django.contrib.auth.decorators import login_required



@login_required
def ticket_details(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    t = User.objects.get(username=ticket.created_by)
    tickets_per_user = t.created_by.all()
    context = {'ticket':ticket, 'tickets_per_user':tickets_per_user  }
    return render(request, 'ticket/ticket_details.html', context)




"""For Staff"""

#creating a ticket
@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.user
            var.ticket_status = 'Pending'
            var.save()
            messages.info(request, 'Your ticket has been successfuly created. An engineer will be assigned to you soon')
            return redirect('dashboard')
        else: 
            messages.warning(request, 'Something went wrong, Please check form input.')
            return redirect('create-ticket')
    else:
        form = CreateTicketForm()
        context= {'form':form}
        return render(request, 'ticket/create-ticket.html', context)


#Updateing the ticket

@login_required
def update_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    if not ticket.is_resolved:
        if request.method == 'POST':
            form = UpdateTicketForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                messages.info(request, 'Your ticket has been updated and changes have been saved.')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Something went wrong. Please check the form input.')
                return redirect('create-ticket')
        else:
            form = UpdateTicketForm(instance=ticket)
        
        context = {'form': form}
        return render(request, 'ticket/update-ticket.html', context)
    else:
        messages.info(request, 'You cannot make any changes.')
        return redirect('dashboard')
    

#view all ticket created

@login_required
def all_tickets(request):
    tickets = Ticket.objects.filter(created_by=request.user).order_by('-date_created')
    context = {'tickets':tickets}
    return render(request, 'ticket/all_tickets.html', context) 


"""For Engineer """

# view ticket queue

@login_required
def ticket_queue(request):
    tickets = Ticket.objects.filter(ticket_status='Pending').order_by('-date_created')
    context = {'tickets': tickets}
    return render(request, 'ticket/ticket_queue.html', context)

#accept a ticket from the queue

@login_required
def accept_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.assigned_to = request.user
    ticket.ticket_status = 'Active'
    ticket.date_accepted = datetime.datetime.now()
    ticket.save()
    messages.info(request, 'Ticket has be accepted. Please resolve as soon a possible!')
    return redirect('workspace')


# close a ticket

@login_required
def close_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.ticket_status = 'Completed'
    ticket.is_resolved = True
    ticket.date_closed = datetime.datetime.now()
    ticket.save()
    messages.info(request, 'Ticket has been resolved. Thank you Support Engineer!')
    return redirect('ticket-queue')


# ticket engineer is working on

@login_required
def workspace(request):
    tickets = Ticket.objects.filter(assigned_to=request.user, is_resolved= False)
    context = {'tickets': tickets}
    return render(request, 'ticket/workspace.html', context)


# all colsed/resolved tickets

@login_required
def all_closed_ticket(request):
    tickets = Ticket.objects.filter(assigned_to=request.user, is_resolved= True)
    context = {'tickets': tickets}
    return render(request, 'ticket/all_closed_ticket.html', context)


