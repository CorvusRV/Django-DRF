from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, SmsCode


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['id', 'phone', 'user_code', 'invite_code', 'staff', 'is_active']
    list_filter = ['phone', 'invite_code', 'staff', 'is_active']
    list_editable = ['user_code', 'invite_code']
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Permissions', {'fields': ('staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2', 'staff', 'is_active')}
         ),
    )
    search_fields = ('phone',)
    ordering = ('phone',)
    filter_horizontal = ()

@admin.register(SmsCode)
class SmsToken(admin.ModelAdmin):
    list_display = ['id', 'phone', 'sms_code', 'sms_active', 'created']
    list_filter = ['phone', 'sms_active']


admin.site.register(CustomUser, CustomUserAdmin)
