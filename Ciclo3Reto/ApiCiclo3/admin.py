from django.contrib import admin
from .models import Profile,Transaction,Enterprise,Rol,Employee

admin.site.register(Profile)
admin.site.register(Transaction)
admin.site.register(Enterprise)
admin.site.register(Rol)
admin.site.register(Employee)