from django.contrib import admin

from users.models import CustomUser, Payment

admin.site.register(CustomUser)
admin.site.register(Payment)
