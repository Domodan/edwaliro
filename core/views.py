import json
import requests
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse

from core.forms import *

# Index views.
def index(request):

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
    print("Enter Profiles")

    url = 'https://api.thingspeak.com/channels/1596329/feeds.json?api_key=PY5EDT094TON962X&results=5'
    data = requests.get(url).json()
    print("Thingspeak Data:", data['feeds'][3])

    return render(request, "core/doctor_profile.html",
        {
            "page": "profile",
            "profile": "profile",
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
    print("Enter Profiles")
    return render(request, "core/nurse_profile.html",
        {
            "page": "profile",
            "profile": "profile",
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
    print("Enter Profiles")
    return render(request, "core/caretaker_profile.html",
        {
            "page": "profile",
            "profile": "profile",
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
    print("Enter Profiles")
    return render(request, "core/patient_profile.html",
        {
            "page": "profile",
            "profile": "profile",
        }
    )


# Login views.
def user_login(request):
    if request.method == 'GET':
        print("It's a get method")
    
    if request.method == 'POST':
        print("It's a post method")
        return HttpResponseRedirect(reverse('index'))
    
    return render(request, 'core/login.html',
        {
            'patient': 'patient',
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
    
    data = json.loads(request.body)

    base_url = 'https://sms.dmarkmobile.com/v2/'
    api_endpoint = 'api/send_sms/'
    url = base_url + api_endpoint

    spname_username = 'makuni'
    sppass_password = 'dicts'

    sender = 8008
    number = data['numbers']
    message = data['messages']
    type = 'json'

    params = {
        'spname': spname_username,
        'sppass': sppass_password
    }
    params = json.dumps(params)

    data = {
        'sender': sender,
        'numbers': number,
        'msg': message,
        'type': type,
    }
    data = json.dumps(data)

    header = {
        'Content-Type': 'application/json'
    }
    
    sample_call = 'https://sms.dmarkmobile.com/v2/api/send_sms/?spname=makuni&sppass=dicts&sender=8008&numbers=256776499859&msg=' + message + '&type=json'

    response = requests.post(url=sample_call)

    if response.status_code == 200:
        json_data = response.json()
        print("Returned JSON Data:", json_data)
        status = json_data['Error']
        print("Status: %s", status)
        if(status):
            return JsonResponse({"error": status})
        return JsonResponse({"success":"SMS sent successfully"})
    else:
        print("Couldn't send SMS")
        print("Response:", response)
        return JsonResponse({"error": response})


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
