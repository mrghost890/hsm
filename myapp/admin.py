from django.contrib import admin
from .models import Signup,Patient

# Register your models here.
class SignupAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','email','state','password','number','Address']
admin.site.register(Signup,SignupAdmin)

class PatientAdmin(admin.ModelAdmin):
    list_display=['fullname','patientemail','patientdate','department','patientnumber','patientmessage']
admin.site.register(Patient,PatientAdmin)