from django.contrib import admin
from .models import patient , doctor , diseaseinfo , consultation,rating_review

# Register your models here.
class AdminDoctor(admin.ModelAdmin):
    list_display=['user','name']
class AdminPatient(admin.ModelAdmin):
    list_display=['user']

admin.site.register(patient,AdminPatient)
admin.site.register(doctor,AdminDoctor)
admin.site.register(diseaseinfo)
admin.site.register(consultation)
admin.site.register(rating_review)