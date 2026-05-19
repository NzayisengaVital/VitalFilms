from django.contrib import admin
from .models import Usermodel, Projectmodel, Contact


# Register your models here.
admin.site.register(Usermodel )
admin.site.register(Projectmodel)
admin.site.register(Contact)