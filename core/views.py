import json
import requests
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
import urllib

from core.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Index views.
def index(request):
    
    instance_id = request.session.get('user_id', None)

    patient_id = request.session.get('patient_id', None)
    nurse_id = request.session.get('nurse_id', None)
    doctor_id = request.session.get('doctor_id', None)
    caretaker_id = request.session.get('caretaker_id', None)

    if instance_id or patient_id or nurse_id or doctor_id or caretaker_id:
        print("Authenticated User:")

        '''
        {'id': 1596329, 'name': 'iDwaliro', 'description': 'A Telehealth channel',
        'latitude': '0.0', 'longitude': '0.0', 'field1': 'Temperature', 'field2': 'Humidity',
        'field3': 'HIC (Heat Index)', 'field4': 'Heart Rate', 'field5': 'Oxygen Level',
        'field6': 'Body Temperature', 'field7': 'Test Field', 'created_at': '2021-12-04T09:33:45Z',
        'updated_at': '2022-02-14T05:55:17Z', 'last_entry_id': 299}
        '''

        url = 'https://api.thingspeak.com/channels/1596329/feeds.json?api_key=PY5EDT094TON962X&results=5'
        response = requests.get(url).json()
        data = response['feeds'][3]

        return render(request, 'core/index.html',
            {
                'data': data,
                'page': 'home',
            }
        )
    else:
        print("None Authenticated User:")

        return render(request, 'core/login.html',
            {
                'login': 'home',
            }
        )


# General Login Views
def user_login(request):
    if request.method == 'GET':
        print("It's a get method")
    
    if request.method == 'POST':
        print("Request Method:", request.POST)
        action = request.POST.get('action', None)
        print("Action:", action)
        if action in ['doctor', 'nurse', 'caretaker']:
            print("Action in Doctor, Nurse, Caretaker:", action)
            if action == 'doctor':
                print("Post Doctor:", request.POST)
                doctor_form = Doctor_Login(request.POST)
                if doctor_form.is_valid():
                    nin = doctor_form.cleaned_data.get('nin')
                    password = doctor_form.cleaned_data.get('password')
                    try:
                        instance = Doctor.objects.get(nin=nin, password=password)
                        request.session['doctor_id'] = instance.id
                        return HttpResponseRedirect(reverse('index'))
                    except Doctor.DoesNotExist:
                        messages.error( request, "Error, User does not exist, please check and try again" )
                else:
                    messages.error( request, "Error, invalid data, please try again" )
            elif action == 'nurse':
                print("Post Nurse:", request.POST)
                nurse_form = Nurse_Login(request.POST)
                if nurse_form.is_valid():
                    nin = nurse_form.cleaned_data.get('nin')
                    password = nurse_form.cleaned_data.get('password')
                    try:
                        instance = Nurse.objects.get(nin=nin, password=password)
                        request.session['nurse_id'] = instance.id
                        return HttpResponseRedirect(reverse('index'))
                    except Nurse.DoesNotExist:
                        messages.error( request, "Error, User does not exist, please check and try again" )
                else:
                    messages.error( request, "Error, invalid data, please try again" )
            elif action == 'caretaker':
                print("Post Caretaker:", request.POST)
                caretaker_form = Caretaker_Login(request.POST)
                if caretaker_form.is_valid():
                    nin = caretaker_form.cleaned_data.get('nin')
                    password = caretaker_form.cleaned_data.get('password')
                    try:
                        instance = Caretaker.objects.get(nin=nin, password=password)
                        request.session['caretaker_id'] = instance.id
                        return HttpResponseRedirect(reverse('index'))
                    except Caretaker.DoesNotExist:
                        messages.error( request, "Error, User does not exist, please check and try again" )
                else:
                    messages.error( request, "Error, invalid data, please try again" )
        elif action in ['admin']:
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session['user_id'] = user.id
                    return HttpResponseRedirect(reverse('index'))
            else:
                messages.error( request, "Error, User does not exist, please check and try again" )
        else:
            messages.error( request, "Invalid Action: Please Choose a correct Login Action" )
    
    return render(request, 'core/login.html',
        {
            'login': 'login',
        }
    )


# General Logout Views
def user_logout(request):
    
    instance_id = request.session.get('user_id', None)

    patient_id = request.session.get('patient_id', None)
    nurse_id = request.session.get('nurse_id', None)
    doctor_id = request.session.get('doctor_id', None)
    caretaker_id = request.session.get('caretaker_id', None)

    print("Loging Out Admin:", instance_id)

    print("Loging Out Patient:", patient_id)

    print("Loging Out Nurse:", nurse_id)

    print("Loging Out Doctor:", doctor_id)

    print("Loging Out Caretaker:", caretaker_id)


# Doctor views.
def doctor(request):
    if request.method == 'POST':
        print("It's a post method")
    else:
        doctor = Doctor.objects.all()

    return render(request, 'core/doctor.html',
        {
            'doctor': doctor,
            'page': 'doctor',
        }
    )

def doctor_add(request):
    if request.method == 'POST':
        doctor = Doctor_Form(request.POST, request.FILES)
        if doctor.is_valid():
            password = doctor.cleaned_data['password']
            password2 = doctor.cleaned_data['password2']
            if password == password2:
                doctor.save()
                return HttpResponseRedirect(reverse('doctor'))
            else:
                return render(request, 'core/doctor_add.html',
                    {
                        'doctor': doctor,
                        'page': 'doctor_add',
                        'error_message': "Two passwords doesnot match, please try again"
                    }
                )
        else:
            return render(request, 'core/doctor_add.html',
                {
                    'doctor': doctor,
                    'page': 'doctor_add',
                    'error_message': "Error, could not add doctor, please try again"
                }
            )
    else:
        doctor = Doctor_Form()
        print("It's a get method")
    
    return render(request, 'core/doctor_add.html',
        {
            'doctor': doctor,
            'page': 'doctor_add',
        }
    )

def doctor_edit(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    doctor_form = Update_Doctor_Form(instance=doctor)
    
    if request.method == 'POST':
        doctor_form = Update_Doctor_Form(request.POST, request.FILES, instance=doctor)
        if doctor_form.is_valid():
            doctor_form.save()
            return HttpResponseRedirect(reverse('doctor'))
    
    return render(request, 'core/doctor_edit.html',
        {
            'doctor': doctor_form,
            'doctor_id': doctor_id,
            'doctor_name': doctor.first_name,
            'page': 'doctor_edit',
        }
    )

def doctor_delete(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    doctor.delete()
    return HttpResponseRedirect(reverse('doctor'))

def doctor_profile(request, doctor_id):
    is_doctor = False
    is_admin = False

    instance_id = request.session.get('user_id', None)
    instance_doctor = request.session.get('doctor_id', None)
    
    if instance_id:
        doctor = User.objects.get( id = instance_id, is_active = True )
        is_admin = True
    elif instance_doctor:
        doctor = Doctor.objects.get( id = instance_doctor )
        is_doctor = True
    else:
        messages.error( request, "Error, User does not exist, please check and try again" )

    url = 'https://api.thingspeak.com/channels/1596329/feeds.json?api_key=PY5EDT094TON962X&results=5'
    data = requests.get(url).json()
    print("Thingspeak Data:", data['feeds'][3])

    return render(request, "core/doctor_profile.html",
        {
            "page": "doctor_profile",
            "profile": doctor,
            "is_doctor": is_doctor,
            "is_admin": is_admin
        }
    )


# Nurse views.
def nurse(request):
    if request.method == 'POST':
        print("It's a post method")
    else:
        nurse = Nurse.objects.all()
        print("It's a get method")
    
    return render(request, 'core/nurse.html',
        {
            'nurse': nurse,
            'page': 'nurse',
        }
    )

def nurse_add(request):
    if request.method == 'POST':
        nurse = Nurse_Form(request.POST, request.FILES)
        if nurse.is_valid():
            password = nurse.cleaned_data['password']
            password2 = nurse.cleaned_data['password2']
            if password == password2:
                nurse.save()
                return HttpResponseRedirect(reverse('nurse'))
            else:
                return render(request, 'core/nurse_add.html',
                    {
                        'nurse': nurse,
                        'page': 'nurse_add',
                        'error_message': "Two passwords doesnot match, please try again"
                    }
                )
        else:
            return render(request, 'core/nurse_add.html',
                {
                    'nurse': nurse,
                    'error_message': "Error, could not add nurse, please try again"
                }
            )
    else:
        nurse = Nurse_Form()
        print("It's a get method")
    
    return render(request, 'core/nurse_add.html',
        {
            'nurse': nurse,
            'page': 'nurse_add',
        }
    )

def nurse_edit(request, nurse_id):
    nurse = Nurse.objects.get(pk=nurse_id)
    nurse_form = Update_Nurse_Form(instance=nurse)
    
    if request.method == 'POST':
        nurse_form = Update_Nurse_Form(request.POST, request.FILES, instance=nurse)
        if nurse_form.is_valid():
            nurse_form.save()
            return HttpResponseRedirect(reverse('nurse'))
    
    return render(request, 'core/nurse_edit.html',
        {
            'nurse': nurse_form,
            'nurse_id': nurse_id,
            'nurse_name': nurse.first_name,
        }
    )

def nurse_delete(request, nurse_id):
    nurse = Nurse.objects.get(pk=nurse_id)
    nurse.delete()
    return HttpResponseRedirect(reverse('nurse'))

def nurse_profile(request, nurse_id):
    try:
        nurse = Nurse.objects.get(pk=nurse_id)
    except Nurse.DoesNotExist:
        messages.error( request, "Error, User does not exist, please check and try again" )
    return render(request, "core/nurse_profile.html",
        {
            "page": "nurse_profile",
            "profile": nurse,
        }
    )


# Caretaker views.
def caretaker(request):
    if request.method == 'POST':
        print("It's a post method")
    else:
        caretaker = Caretaker.objects.all()
        print("It's a get method")
    
    return render(request, 'core/caretaker.html',
        {
            'caretaker': caretaker,
            'page': 'caretaker',
        }
    )

def caretaker_add(request):
    if request.method == 'POST':
        caretaker = Caretaker_Form(request.POST, request.FILES)
        if caretaker.is_valid():
            password = caretaker.cleaned_data['password']
            password2 = caretaker.cleaned_data['password2']
            if password == password2:
                caretaker.save()
                return HttpResponseRedirect(reverse('caretaker'))
            else:
                return render(request, 'core/caretaker_add.html',
                    {
                        'caretaker': caretaker,
                        'error_message': "Two passwords doesnot match, please try again"
                    }
                )
        else:
            return render(request, 'core/caretaker_add.html',
                {
                    'caretaker': caretaker,
                    'page': 'caretaker_add',
                    'error_message': "Error, could not add caretaker, please try again"
                }
            )
    else:
        caretaker = Caretaker_Form()
    
    return render(request, 'core/caretaker_add.html',
        {
            'caretaker': caretaker,
            'page': 'caretaker_add',
        }
    )

def caretaker_edit(request, caretaker_id):
    caretaker = Caretaker.objects.get(pk=caretaker_id)
    caretaker_form = Update_Caretaker_Form(instance=caretaker)
    
    if request.method == 'POST':
        caretaker_form = Update_Caretaker_Form(request.POST, request.FILES, instance=caretaker)
        if caretaker_form.is_valid():
            caretaker_form.save()
            return HttpResponseRedirect(reverse('caretaker'))
    
    return render(request, 'core/caretaker_edit.html',
        {
            'caretaker': caretaker_form,
            'caretaker_id': caretaker_id,
            'caretaker_name': caretaker.first_name,
            'page': 'caretaker_edit',
        }
    )

def caretaker_delete(request, caretaker_id):
    caretaker = Caretaker.objects.get(pk=caretaker_id)
    caretaker.delete()
    return HttpResponseRedirect(reverse('caretaker'))

def caretaker_profile(request, caretaker_id):
    try:
        caretaker = Caretaker.objects.get(pk=caretaker_id)
    except Caretaker.DoesNotExist:
        messages.error( request, "Error, User does not exist, please check and try again" )
    return render(request, "core/caretaker_profile.html",
        {
            "page": "caretaker_profile",
            "profile": caretaker,
        }
    )


# Patient views.
def patient(request):
    
    if request.method == 'POST':
        print("It's a post method")
    else:
        patient = Patient.objects.all()
    
    return render(request, 'core/patient.html',
        {
            'patient': patient,
            'page': 'patient',
        }
    )

def patient_add(request):
    if request.method == 'POST':
        patient = Patient_Form(request.POST, request.FILES)
        if patient.is_valid():
            password = patient.cleaned_data['password']
            password2 = patient.cleaned_data['password2']
            if password == password2:
                patient.save()
                return HttpResponseRedirect(reverse('patient'))
            else:
                return render(request, 'core/patient_add.html',
                    {
                        'patient': patient,
                        'error_message': "Two passwords doesnot match, please try again"
                    }
                )
        else:
            return render(request, 'core/patient_add.html',
                {
                    'patient': patient,
                    'error_message': "Error, could not add patient, please try again"
                }
            )
    else:
        patient = Patient_Form()
    
    return render(request, 'core/patient_add.html',
        {
            'patient': patient,
            'page': 'patient_add',
        }
    )

def patient_edit(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    patient_form = Update_Patient_Form(instance=patient)
    
    if request.method == 'POST':
        patient_form = Update_Patient_Form(request.POST, request.FILES, instance=patient)
        if patient_form.is_valid():
            patient_form.save()
            return HttpResponseRedirect(reverse('patient'))
    
    return render(request, 'core/patient_edit.html',
        {
            'patient': patient_form,
            'patient_id': patient_id,
            'patient_name': patient.first_name,
            'page': 'patient_edit',
        }
    )

def patient_delete(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    patient.delete()
    return HttpResponseRedirect(reverse('patient'))

def patient_profile(request, patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        messages.error( request, "Error, User does not exist, please check and try again" )
    return render(request, "core/patient_profile.html",
        {
            "page": "patient_profile",
            "profile": patient,
        }
    )


# Forgot assword views.
def forgot_password(request):
    if request.method == 'GET':
        print("It's a get method")
    
    if request.method == 'POST':
        print("It's a post method")
        return HttpResponseRedirect(reverse('index'))
    
    return render(request, 'core/forgot_password.html',
        {
            'patient': 'patient',
        }
    )


# Fetch thingspeak data
def fetch_data(request):

    '''
    {'id': 1596329, 'name': 'iDwaliro', 'description': 'A Telehealth channel',
    'latitude': '0.0', 'longitude': '0.0', 'field1': 'Temperature', 'field2': 'Humidity',
    'field3': 'HIC (Heat Index)', 'field4': 'Heart Rate', 'field5': 'Oxygen Level',
    'field6': 'Body Temperature', 'field7': 'Test Field', 'created_at': '2021-12-04T09:33:45Z',
    'updated_at': '2022-02-14T05:55:17Z', 'last_entry_id': 299}
    '''

    url = 'https://api.thingspeak.com/channels/1596329/feeds.json?api_key=PY5EDT094TON962X&results=5'
    response = requests.get(url).json()
    data = response['feeds']

    return render(request, 'core/index.html',
        {
            'data': data,
            'page': 'home',
        }
    )


# Send SMS
def send_sms(request):

    '''
    MAKERERE UNI DICTS LOGINS

    Account Login
    URL: https://sms.dmarkmobile.com/v2/
    Username: makuni
    Pass: dicts

    API END-POINT
    https://sms.dmarkmobile.com/v2/api/send_sms/?
    spname=makuni&sppass=dicts&sender=8008&numbers=256xxxxxxxxx&msg=testing&type=json

    https://sms.dmarkmobile.com/v2/api/send_sms/?
    spname=makuni&sppass=dicts&numbers=0789157162
    &msg="Abnormal Body Temperature of 29.19 detected"&type=json

    https://sms.dmarkmobile.com/v2/api/send_sms/?
    spname=username***&sppass=password***&numbers=256787550983,256754033432
    &msg=testing%20API%20SMS%20delivery&type=json


    https://sms.dmarkmobile.com/v2/api/acc_bal/?spname=username***&sppass=password***

    https://sms.dmarkmobile.com/v2/api/acc_bal/?spname=makuni&sppass=dicts
    
    '''
    
    data = json.loads(request.body)

    number = data['numbers']
    message = data['messages']

    print("Request Message:", message)

    patient = Patient.objects.get()
    message += " " + patient.nin
    
    message = urllib.parse.quote(message)

    print("Message:", message)
    
    username = 'makuni'
    password = 'dicts'
    types = 'json'

    base_url = 'https://sms.dmarkmobile.com/v2/api/'
    api_endpoint_send_sms = 'send_sms/?'

    spname = 'spname=' + username
    sppass = '&sppass=' + password
    numbers = '&numbers=' + number
    msg = '&msg=' + message
    type = '&type=' + types

    url_send_sms = base_url + api_endpoint_send_sms + spname + sppass
    url_send_sms += numbers + msg + type

    print("API URL:", url_send_sms)
    
    response = requests.get(url=url_send_sms)

    if response.status_code == 200:
        json_data = response.json()
        print("JSON Response:", json_data)
        return JsonResponse(json_data)
    else:
        print("Couldn't send SMS")
        return JsonResponse({"Error": "Could Not Send SMS", "Response": response})


# Testing
def test_work(request):

    '''
    {'id': 1596329, 'name': 'iDwaliro', 'description': 'A Telehealth channel',
    'latitude': '0.0', 'longitude': '0.0', 'field1': 'Temperature', 'field2': 'Humidity',
    'field3': 'HIC (Heat Index)', 'field4': 'Heart Rate', 'field5': 'Oxygen Level',
    'field6': 'Body Temperature', 'field7': 'Test Field', 'created_at': '2021-12-04T09:33:45Z',
    'updated_at': '2022-02-14T05:55:17Z', 'last_entry_id': 299}
    '''

    url = 'https://api.thingspeak.com/channels/1596329/feeds.json?api_key=PY5EDT094TON962X&results=5'
    response = requests.get(url).json()
    data = response['feeds']

    return render(request, 'core/test.html',
        {
            'data': data,
            'page': 'home',
        }
    )
