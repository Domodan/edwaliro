from django.urls import path
from core.views import *


urlpatterns = [
    path('', index, name='index'),
    path('doctor/', doctor, name='doctor'),
    path('doctor_add/', doctor_add, name='doctor_add'),
    path('doctor_edit/<int:doctor_id>/', doctor_edit, name='doctor_edit'),
    path('doctor_delete/<int:doctor_id>/', doctor_delete, name='doctor_delete'),
    path('doctor_profile/<int:doctor_id>/', doctor_profile, name='doctor_profile'),

    path('nurse/', nurse, name='nurse'),
    path('nurse_add/', nurse_add, name='nurse_add'),
    path('nurse_edit/<int:nurse_id>/', nurse_edit, name='nurse_edit'),
    path('nurse_delete/<int:nurse_id>/', nurse_delete, name='nurse_delete'),
    path('nurse_profile/<int:nurse_id>/', nurse_profile, name='nurse_profile'),

    path('caretaker/', caretaker, name='caretaker'),
    path('caretaker_add/', caretaker_add, name='caretaker_add'),
    path('caretaker_edit/<int:caretaker_id>/', caretaker_edit, name='caretaker_edit'),
    path('caretaker_delete/<int:caretaker_id>/', caretaker_delete, name='caretaker_delete'),
    path('caretaker_profile/<int:caretaker_id>/', caretaker_profile, name='caretaker_profile'),

    path('patient/', patient, name='patient'),
    path('patient_add/', patient_add, name='patient_add'),
    path('patient_edit/<int:patient_id>/', patient_edit, name='patient_edit'),
    path('patient_delete/<int:patient_id>/', patient_delete, name='patient_delete'),
    path('patient_profile/<int:patient_id>/', patient_profile, name='patient_profile'),

    path('login/', user_login, name='login'),
    path('send_sms/', send_sms, name='send_sms'),
    path('test_work/', test_work, name='test_work'),
    path('forgot_password/', forgot_password, name='forgot_password'),
]