from django.contrib import admin
from cuser.admin import UserAdmin
from .models import User, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 1
    fields = ['user', 'bio', 'image']

class CustomUserAdmin(UserAdmin):
    inlines = [
        ProfileInline,
    ]

class ProfileAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
            qs = super(ProfileAdmin, self).get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(user=request.user)

    def get_form(self, request, obj=None, **kwargs):
            if request.user.is_superuser:
                self.exclude = ()
            else:
                self.exclude = ('user',) 
            return super(ProfileAdmin, self).get_form(request, obj=None, **kwargs) 
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.user = request.user
            super().save_model(request, obj, form, change)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)