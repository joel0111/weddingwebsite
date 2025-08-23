from django import forms
from django.utils.translation import gettext_lazy as _
from .models import RSVP, Volunteer, VolunteerRole

class RSVPForm(forms.ModelForm):
    RESERVATION_REASON_CHOICES = [
        ('', _('Select a reason')),
        ('mobility', _('Mobility issues / wheelchair access')),
        ('elderly', _('Elderly passenger')),
        ('pregnant', _('Pregnant passenger')),
        ('young_children', _('Young children / infants')),
        ('medical', _('Medical condition')),
        ('heavy_items', _('Bringing heavy items')),
        ('other', _('Other (please specify in comments)')),
    ]
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
    name = forms.CharField(label=_("Name"), widget=forms.TextInput(attrs={'class': 'rsvp-input'}))
    email = forms.EmailField(required=False, label=_("Email"), widget=forms.EmailInput(attrs={'class': 'rsvp-input'}))
    attending = forms.BooleanField(required=False, widget=forms.RadioSelect(choices=[(True, _('Yes')), (False, _('No'))]))
    message = forms.CharField(required=False, label=_("Write your well wishes for the couple:"), widget=forms.Textarea(attrs={'class': 'rsvp-input'}))
    connected_to = forms.ChoiceField(choices=RSVP.CONNECTION_CHOICES, widget=forms.RadioSelect)
    dietary_preferences = forms.ChoiceField(choices=DIETARY_CHOICES, required=False, initial='none', widget=forms.Select(attrs={'class': 'rsvp-input'}))
    food_allergies = forms.ChoiceField(choices=ALLERGY_CHOICES, required=False, initial='none', widget=forms.Select(attrs={'class': 'rsvp-input'}))
    other_comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'rsvp-input'}))
    carpark_slot_reservation = forms.BooleanField(required=False, widget=forms.RadioSelect(choices=[(True, _('Yes')), (False, _('No'))]))
    car_plate_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'rsvp-input'}))
    reservation_reason = forms.ChoiceField(
        choices=RESERVATION_REASON_CHOICES,
        required=False,
        label=_("Reason for Carpark Reservation"),
        widget=forms.Select(attrs={'id': 'id_reservation_reason', 'style': 'width:100%; padding:8px; border-radius:8px; border:1px solid #d6336c; color:#243c5a; font-size:1em;'})
    )
    class Meta:
        model = RSVP
        fields = ['name', 'email', 'contact_number', 'attending', 'message', 'connected_to', 'dietary_preferences', 'food_allergies', 'other_comments', 'carpark_slot_reservation', 'car_plate_number', 'reservation_reason']

class VolunteerForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        label=_("Name"),
        widget=forms.TextInput(attrs={'placeholder': 'E.g. John'})
    )
    email = forms.EmailField(
        required=True,
        label=_("Email"),
        widget=forms.EmailInput(attrs={'placeholder': 'E.g. john@gmail.com'})
    )
    contact_number = forms.CharField(
        required=True,
        label=_("Contact Number"),
        widget=forms.TextInput(attrs={'placeholder': 'E.g. 9123 4567'})
    )
    # Safe default queryset; real queryset set in __init__
    roles = forms.ModelMultipleChoiceField(
        queryset=VolunteerRole.objects.none(),
        required=True,
        label=_("Roles you'd like to help with")
    )

    class Meta:
        model = Volunteer
        fields = ['name', 'email', 'contact_number', 'roles', 'role_details', 'comments']
        labels = {
            'name': _("Name"),
            'email': _("Email"),
            'contact_number': _("Contact Number"),
            'role_details': _("Role Details"),
            'comments': _("Comments"),
            'roles': _("How would you like to help?")
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _("E.g. John")}),
            'email': forms.EmailInput(attrs={'placeholder': _("E.g. john@gmail.com")}),
            'role_details': forms.Textarea(attrs={'placeholder': _("Provide any details about your selected roles"), 'rows': 4, 'id': 'id_role_details'}),
            'comments': forms.Textarea(attrs={'placeholder': _("Any comments or questions?")}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Lazily populate roles queryset; avoid 500 if table is missing
        try:
            self.fields['roles'].queryset = VolunteerRole.objects.all().order_by('name')
        except Exception:
            self.fields['roles'].queryset = VolunteerRole.objects.none()
