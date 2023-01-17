from django.contrib import admin
from .models import Person, SportClub, Tournament, Results
# Register your models here.

admin.site.register(Person)
admin.site.register(SportClub)
admin.site.register(Tournament)
admin.site.register(Results)

