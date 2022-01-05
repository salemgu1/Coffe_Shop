from django.contrib import admin

from .models import Coffee, Customer


class MovieAdmin(admin.ModelAdmin):
    pass


admin.site.register(Coffee, MovieAdmin)


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)
