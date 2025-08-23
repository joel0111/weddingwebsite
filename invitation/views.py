from django.shortcuts import render, redirect
from .models import RSVP, VolunteerRole
from .forms import RSVPForm, VolunteerForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

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
            # Send notification email for RSVP
            subject = f"New RSVP from {rsvp.name}"
            message = (
                f"Name: {rsvp.name}\n"
                f"Email: {rsvp.email}\n"
                f"Contact Number: {rsvp.contact_number}\n"
                f"Attending: {rsvp.attending}\n"
                f"Connected To: {rsvp.connected_to}\n"
                f"Dietary Preferences: {rsvp.dietary_preferences}\n"
                f"Food Allergies: {rsvp.food_allergies}\n"
                f"Other Comments: {rsvp.other_comments}\n"
                f"Carpark Reservation: {rsvp.carpark_slot_reservation}\n"
                f"Car Plate Number: {rsvp.car_plate_number}\n"
                f"Reservation Reason: {rsvp.reservation_reason}\n"
            )
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.NOTIFICATION_EMAIL])
            except Exception as e:
                messages.warning(request, 'Your response was saved, but we could not send the notification email.')
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
            # Send notification email for volunteer
            subject = f"New Volunteer Signup: {volunteer.name}"
            roles = ', '.join([r.name for r in volunteer.roles.all()])
            message = (
                f"Name: {volunteer.name}\n"
                f"Email: {volunteer.email}\n"
                f"Contact Number: {volunteer.contact_number}\n"
                f"Roles: {roles}\n"
                f"Role Details: {volunteer.role_details}\n"
                f"Comments: {volunteer.comments}\n"
            )
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.NOTIFICATION_EMAIL])
            except Exception as e:
                messages.warning(request, 'Your signup was saved, but we could not send the notification email.')
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
