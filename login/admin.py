from django.contrib import admin
from database.models import Registration, Patient, AmbulanceSchedule, AmbulanceBooking,Doctor

admin.site.register(Registration)
admin.site.register(Patient)
admin.site.register(AmbulanceSchedule)
admin.site.register(AmbulanceBooking)
admin.site.register(Doctor)
# Register your models here.
