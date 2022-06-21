from django.contrib import admin

from .models import CustomerRequest, Ministry, RequestStatus

admin.site.register(Ministry)
admin.site.register(CustomerRequest)
admin.site.register(RequestStatus)
