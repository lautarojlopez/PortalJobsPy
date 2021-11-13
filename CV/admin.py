from django.contrib import admin
from CV.models import CV
from usuarios.models import UserProfile

# Register your models here.
admin.site.register(CV)
admin.site.register(UserProfile)
