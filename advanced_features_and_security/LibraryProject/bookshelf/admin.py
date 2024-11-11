from django.contrib import admin
from .models import Book


# Register your models here.
from .models import CustomUser

# Register your models here.

admin.site.register(CustomUser, CustomUserManager)
admin.register(Book)

from django.contrib.auth.admin import UserAdmin
from .models import CustomUserManager, CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm

    model = CustomUser

    list_display = ('username', 'email', 'is_superuser', 'last_login',)
    # list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        #  ('Permissions', {'fields': ('is_staff', 'is_active',
        #  'is_superuser', 'groups', 'user_permissions')}),
        ('Permissions', {
         'fields': ('is_superuser', 'groups', 'user_permissions'), }),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            # 'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')
    list_filter = ('publication_year')
