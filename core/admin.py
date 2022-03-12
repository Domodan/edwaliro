from django.contrib import admin
from core.models import Caretaker, Doctor, Nurse, Patient


# Register Doctor model.
class Doctor_Admin(admin.ModelAdmin):
    fields = [ 'first_name', 'last_name', 'email', 'phone_number', 'password', 'nin', 'gender', 'avatar' ]

    list_display = ( 'first_name', 'last_name', 'email', 'phone_number', 'password', 'nin', 'gender', 'avatar' )

admin.site.register(Doctor, Doctor_Admin)


# Register Nurse model.
class Nurse_Admin(admin.ModelAdmin):
    fields = [ 'first_name', 'last_name', 'email', 'phone_number', 'password', 'nin', 'gender', 'avatar' ]

    list_display = ( 'first_name', 'last_name', 'email', 'phone_number', 'password', 'nin', 'gender', 'avatar' )

admin.site.register(Nurse, Nurse_Admin)


# Register Caretaker model.
class Caretaker_Admin(admin.ModelAdmin):
    fields = [ 'first_name', 'last_name', 'email', 'phone_number', 'password', 'nin', 'gender', 'avatar' ]

    list_display = ( 'first_name', 'last_name', 'email', 'phone_number', 'password', 'nin', 'gender', 'avatar' )

admin.site.register(Caretaker, Caretaker_Admin)


# Register Patient model.
class Patient_Admin(admin.ModelAdmin):

    fields = [ 'doctor', 'nurse', 'caretaker', 'first_name', 'last_name', 'phone_number', 'password',
    'nin', 'weight', 'gender', 'avatar'
    ]
    list_display =  ( 'doctor', 'nurse', 'caretaker', 'first_name', 'last_name', 'phone_number', 'password',
    'nin', 'weight', 'gender', 'avatar'
    )

admin.site.register(Patient, Patient_Admin)

