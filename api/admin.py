from django.contrib import admin
from .models import Step, FinalStep, Choice, FirstStep

# Register your models here.
admin.site.register(Step)
admin.site.register(FinalStep)
admin.site.register(Choice)
admin.site.register(FirstStep)
