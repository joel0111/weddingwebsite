from django.contrib import admin
from .models import RSVP, Volunteer, VolunteerRole

class RSVPAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'attending', 'connected_to_display', 'dietary_preferences',
        'food_allergies', 'carpark_slot_reservation', 'car_plate_number', 'reservation_reason'
    )
    list_filter = ('attending', 'connected_to', 'dietary_preferences', 'food_allergies', 'carpark_slot_reservation')
    search_fields = ('name', 'email', 'car_plate_number')
    readonly_fields = ()

    def connected_to_display(self, obj):
        if obj.connected_to == 'groom':
            return 'Joel'
        elif obj.connected_to == 'bride':
            return 'Amanda'
        elif obj.connected_to == 'both':
            return 'Both'
        return obj.connected_to
    connected_to_display.short_description = 'Connected To'

admin.site.register(RSVP, RSVPAdmin)

class VolunteerAdmin(admin.ModelAdmin):
    exclude = ('phone', 'role_details')

admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(VolunteerRole)
