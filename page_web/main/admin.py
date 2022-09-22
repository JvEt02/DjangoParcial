
"""
Aqui hacemos la importacion de las librerias y los models  para mandarlos al http de admin
para cualquier tipo de modificacion o creacion de contenido de la pagina, al igual que poder
administrar los usuarios y muchas cosas mas en la page web.
"""
from django.contrib import admin
from . models import (
    UserProfile,
    ContactProfile,
    Blog,
    Review 
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'timestamp', 'name',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Review)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)
