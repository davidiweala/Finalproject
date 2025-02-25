from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AdminUser


class Admin(UserAdmin):
    list_filter = ('first_name', 'last_name', 'username', 'email', 'phone', 'date_joined', 'last_login')
    search_fields = ('email', 'username', 'last_name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(AdminUser, Admin)
