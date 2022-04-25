from django.contrib.auth.models import User
from core.models import Patient, Doctor, Nurse, Caretaker

def extras(request):
    
    instance_id = request.session.get('user_id', None)

    patient_id = request.session.get('patient_id', None)
    nurse_id = request.session.get('nurse_id', None)
    doctor_id = request.session.get('doctor_id', None)
    caretaker_id = request.session.get('caretaker_id', None)

    instance = None
    instance_patient = None
    instance_nurse = None
    instance_doctor = None
    instance_caretaker = None

    try:
        try:
            instance = User.objects.get( id = instance_id, is_active = True ) if instance_id is not None else None
            print("Admin Instance:", instance.first_name)
        except:
            del request.session['user_id']

        try:
            instance_patient = Patient.objects.get( id = patient_id, is_active = True ) if patient_id is not None else None
        except:
            del request.session['patient_id']
            
        try:
            instance_nurse = Nurse.objects.get( id = nurse_id, is_active = True ) if nurse_id is not None else None
        except:
            del request.session['nurse_id']
            
        try:
            instance_doctor = Doctor.objects.get( id = doctor_id, is_active = True ) if doctor_id is not None else None
        except:
            del request.session['doctor_id']
            
        try:
            instance_caretaker = Caretaker.objects.get( id = caretaker_id, is_active = True ) if caretaker_id is not None else None
        except:
            del request.session['caretaker_id']
    except:
        pass

    custom = {
        'admin': instance,
        'patient': instance_patient,
        'nurse': instance_nurse,
        'doctor': instance_doctor,
        'caretaker': instance_caretaker
    }

    return custom
