from django.contrib import admin
from database.models import Registration, Patient, AmbulanceSchedule

admin.site.register(Registration)
admin.site.register(Patient)
admin.site.register(AmbulanceSchedule)
# Register your models here.
