from django.contrib import admin
from database.models import Registration, Patient, AmbulanceSchedule, AmbulanceBooking

admin.site.register(Registration)
admin.site.register(Patient)
admin.site.register(AmbulanceSchedule)
admin.site.register(AmbulanceBooking)
# Register your models here.
