from django.contrib import admin

from .models import csvmodel, valueModel
admin.site.register(csvmodel)
admin.site.register(valueModel)