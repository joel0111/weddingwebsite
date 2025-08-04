from django.shortcuts import render, redirect
from .models import RSVP, VolunteerRole
from .forms import RSVPForm, VolunteerForm
from django.contrib import messages

def home(request):
    return render(request, 'invitation/home.html')

def rsvp(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            rsvp = form.save(commit=False)
            rsvp.contact_number = request.POST.get('contact_number', '')
            # Manually assign custom field values from POST
            rsvp.dietary_preferences = request.POST.get('dietary', '')
            rsvp.food_allergies = request.POST.get('allergies', '')
            rsvp.other_comments = request.POST.get('comments', '')
            carpark_reservation = request.POST.get('carpark_reservation', 'no')
            rsvp.carpark_slot_reservation = (carpark_reservation == 'yes')
            rsvp.car_plate_number = request.POST.get('carplate', '')
            rsvp.reservation_reason = request.POST.get('reservation_reason', '')
            rsvp.save()
            return redirect('rsvp_thanks')
    else:
        form = RSVPForm()
    return render(request, 'invitation/rsvp.html', {'form': form})

def rsvp_thanks(request):
    return render(request, 'invitation/rsvp_thanks.html')

def heart_gate(request):
    return render(request, 'invitation/heart_gate.html')

def gallery(request):
    return render(request, 'invitation/gallery.html')

def volunteer(request):
    selected_roles = []
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        selected_roles = request.POST.getlist('roles')
        if form.is_valid():
            volunteer = form.save(commit=False)
            volunteer.save()
            form.save_m2m()
            return redirect('volunteer_thanks')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = VolunteerForm()
        if hasattr(form, 'initial') and 'roles' in form.initial:
            selected_roles = [str(r) for r in form.initial['roles']]
    return render(request, 'invitation/volunteer.html', {'form': form, 'selected_roles': selected_roles})

def volunteer_thanks(request):
    return render(request, 'invitation/volunteer_thanks.html')

def freebies(request):
    return render(request, 'invitation/freebies.html')
