from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Event

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('id','email', 'phone_number', 'is_staff','password','business_name')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone_number')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'phone_number',)
    ordering = ('email',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=['id','title','description','date','EventType']
    


admin.site.register(User, CustomUserAdmin)

# admin.site.register(Event)