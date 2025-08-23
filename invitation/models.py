from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class RSVP(models.Model):
    name = models.CharField(_("Your Name"), max_length=100, blank=False, null=False)
    email = models.EmailField(_("Your Email"), blank=True, null=True)
    contact_number = models.CharField(_("Contact Number"), max_length=20, blank=True, null=True)
    attending = models.BooleanField(_("Attending"), blank=False, null=False)
    message = models.TextField(_("Message"), blank=True, null=True)
    CONNECTION_CHOICES = [
        ('bride', _('Amanda')),
        ('groom', _('Joel')),
        ('both', _('Both')),
    ]
    connected_to = models.CharField(_("Connected to"), max_length=10, choices=CONNECTION_CHOICES, default='both', blank=False, null=False)
    DIETARY_CHOICES = [
        ('dairy_free', _('Dairy-Free')),
        ('gluten_free', _('Gluten-Free')),
        ('halal', _('Halal')),
        ('no_beef', _('No Beef')),
        ('no_seafood', _('No seafood')),
        ('none', _('No preference')),
        ('nut_free', _('Nut-Free')),
        ('other', _('Other (please specify in comments)')),
        ('vegan', _('Vegan')),
        ('vegetarian', _('Vegetarian')),
    ]
    dietary_preferences = models.CharField(_("Dietary Preferences"), max_length=255, blank=True, null=True, choices=DIETARY_CHOICES)
    ALLERGY_CHOICES = [
        ('dairy_free', _('Dairy-Free')),
        ('eggs', _('Eggs')),
        ('fish', _('Fish')),
        ('milk', _('Milk')),
        ('none', _('No allergies')),
        ('other', _('Other (please specify in comments)')),
        ('peanuts', _('Peanuts')),
        ('sesame', _('Sesame')),
        ('shellfish', _('Shellfish')),
        ('soy', _('Soy')),
        ('tree_nuts', _('Tree Nuts')),
        ('wheat', _('Wheat')),
    ]
    food_allergies = models.CharField(_("Food Allergies"), max_length=255, blank=True, null=True, choices=ALLERGY_CHOICES)
    other_comments = models.TextField(_("Other Comments"), blank=True, null=True)
    carpark_slot_reservation = models.BooleanField(_("Carpark Slot Reservation"), default=False)
    car_plate_number = models.CharField(_("Car Plate Number"), max_length=20, blank=True, null=True)
    reservation_reason = models.TextField(_("Reservation Reason"), blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({'Attending' if self.attending else 'Not Attending'})"

class VolunteerRole(models.Model):
    ROLE_CHOICES = [
        ('usher', _('Usher')),
        ('photography', _('Photography')),
        ('videography', _('Videography')),
        ('worship', _('Worship')),
        ('setup', _('Setup')),
        ('teardown', _('Teardown')),
        ('carpark', _('Carpark')),
        ('screens', _('Screens')),
        ('lights', _('Lights')),
        ('sound', _('Sound')),
    ]
    name = models.CharField(max_length=20, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()

class Volunteer(models.Model):
    name = models.CharField(_("Your Name"), max_length=100)
    email = models.EmailField(_("Your Email"))
    phone = models.CharField(_("Phone"), max_length=20, blank=True)
    contact_number = models.CharField(_("Contact Number"), max_length=20, blank=True)
    comments = models.TextField(_("Comments"), blank=True)  # Renamed from message to comments
    roles = models.ManyToManyField(VolunteerRole, blank=True)
    role_details = models.TextField(blank=True, null=True, default='')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
