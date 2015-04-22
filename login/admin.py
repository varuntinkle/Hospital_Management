from django.contrib import admin
from database.models import Finance_accountant,Internal_rim, Registration, Patient, AmbulanceSchedule, AmbulanceBooking,Doctor

admin.site.register(Registration)
admin.site.register(Patient)
admin.site.register(AmbulanceSchedule)
admin.site.register(AmbulanceBooking)
admin.site.register(Doctor)
admin.site.register(Internal_rim)
admin.site.register(Finance_accountant)
# Register your models here.
