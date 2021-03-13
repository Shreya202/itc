from django.contrib import admin
from .models import Candidate, Panelist, PanelistSchedule, Interview

# Register your models here.

admin.site.register(Candidate)
admin.site.register(Panelist)
admin.site.register(PanelistSchedule)
admin.site.register(Interview)
