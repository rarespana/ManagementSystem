from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, County


class CountyInline(admin.TabularInline):
    model = County.admins.through

class AdminUser(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone', 'state')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email',
                       'first_name', 'last_name', 'phone', 'state'),
        }),
    )

    list_display = ('username', 'email', 'last_name', 'first_name', 'phone', 'state', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'state')
    ordering = ('username',)

    inlines = [CountyInline]


admin.site.register(User, AdminUser)

class CountyAdmin(admin.ModelAdmin):
    fields = [
        'county_name',
    ]

    ordering = ('county_name',)

admin.site.register(County, CountyAdmin)
