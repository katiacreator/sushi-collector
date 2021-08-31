from django.contrib import admin
# import your models here
from .models import Sushi, Side

# Register your models here
admin.site.register(Sushi)
admin.site.register(Side)
