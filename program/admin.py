from django.contrib import admin
from .models import Program
from .models import Recommendation

# Register your models here.
admin.site.register(Program)
admin.site.register(Recommendation)