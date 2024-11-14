from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Propriedade, Municipio, Proprietario, ProprietarioPropriedade, CNPJ, Titular

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('first_name', 'last_name', 'email', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('perfil', 'tipo', 'first_name', 'last_name')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'perfil', 'tipo', 'first_name', 'last_name'),
        }),
    )


@admin.register(Propriedade)
class PropriedadeAdmin(admin.ModelAdmin):
    list_display = ()


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ()


@admin.register(Proprietario)
class ProprietarioAdmin(admin.ModelAdmin):
    list_display = ()


@admin.register(ProprietarioPropriedade)
class ProprietarioPropriedadeAdmin(admin.ModelAdmin):
    list_display = ()


@admin.register(CNPJ)
class CNPJAdmin(admin.ModelAdmin):
    list_display = ()


@admin.register(Titular)
class TitularAdmin(admin.ModelAdmin):
    list_display = ()