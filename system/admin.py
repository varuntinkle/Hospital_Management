from django.contrib import admin

from database.models import Medicine, CRequest,Registration,Post, Doctor,AmbulanceBooking,AmbulanceSchedule, Reception,Patient, Prescription, FollowUp, Complaint

admin.site.register(Medicine)
admin.site.register(CRequest)
admin.site.register(Reception)
admin.site.register(Prescription)
admin.site.register(FollowUp)
admin.site.register(Complaint)


# Register your models here.
 