from django.contrib import admin

# Register your models here.
from .models import TrainLine, StationList

admin.site.register(TrainLine)
admin.site.register(StationList)