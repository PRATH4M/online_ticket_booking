# booking/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Booking
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def event_list(request):
    events = Event.objects.all()
    return render(request, 'booking/event_list.html', {'events': events})

@login_required
def book_ticket(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Set the user field
            if booking.seats > event.available_seats():
                messages.error(request, 'Not enough available seats')
            else:
                booking.event = event
                booking.save()
                messages.success(request, 'Booking successful')
                return redirect('event_list')
    else:
        form = BookingForm()
    return render(request, 'booking/book_ticket.html', {'form': form, 'event': event})
