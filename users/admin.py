from django.contrib import admin

from payments.models import Payment
from users.models import CustomUser

admin.site.register(CustomUser)
admin.site.register(Payment)
