from django import forms
from django.contrib.auth.models import User
from core.models import Caretaker, Doctor, Nurse, Patient

# Admin Login Form
class Admin_Login(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'username', 'password' ]

# Login Forms Doctor
class Doctor_Login(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [ 'nin', 'password' ]
        widgets = {
            'nin': forms.TextInput(attrs={
                'placeholder': 'National Identity Number',
                'class': 'form-control form-control-user'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password',
                'class': 'form-control form-control-user'
            }),
        }

# Login Forms Nurse
class Nurse_Login(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = [ 'nin', 'password' ]
        widgets = {
            'nin': forms.TextInput(attrs={
                'placeholder': 'National Identity Number',
                'class': 'form-control form-control-user'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password',
                'class': 'form-control form-control-user'
            }),
        }

# Login Forms Caretaker
class Caretaker_Login(forms.ModelForm):
    class Meta:
        model = Caretaker
        fields = [ 'nin', 'password' ]
        widgets = {
            'nin': forms.TextInput(attrs={
                'placeholder': 'National Identity Number',
                'class': 'form-control form-control-user'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password',
                'class': 'form-control form-control-user'
            }),
        }

# Doctor Form
class Doctor_Form(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'class': 'form-control form-control-user'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'class': 'form-control form-control-user'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email Address',
                'class': 'form-control form-control-user'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Phone Number',
                'class': 'form-control form-control-user'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'nin': forms.TextInput(attrs={
                'placeholder': 'National Identity Number',
                'class': 'form-control form-control-user'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password',
                'class': 'form-control form-control-user'
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Repeat Password',
                'class': 'form-control form-control-user'
            }),
            'avatar': forms.FileInput()
        }

# Doctor Form
class Update_Doctor_Form(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [ 'first_name', 'last_name', 'email', 'phone_number', 'gender', 'nin', 'avatar' ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'class': 'form-control form-control-user'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'class': 'form-control form-control-user'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email Address',
                'class': 'form-control form-control-user'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Phone Number',
                'class': 'form-control form-control-user'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'nin': forms.TextInput(attrs={
                'placeholder': 'National Identity Number',
                'class': 'form-control form-control-user'
            }),
            'avatar': forms.FileInput()
        }

# Nurse Form
class Nurse_Form(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'class': 'form-control form-control-user'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'class': 'form-control form-control-user'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email Address',
                'class': 'form-control form-control-user'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Phone Number',
                'class': 'form-control form-control-user'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'nin': forms.TextInput(attrs={
                'placeholder': 'National Identity Number',
                'class': 'form-control form-control-user'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password',
                'class': 'form-control form-control-user'
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Repeat Password',
                'class': 'form-control form-control-user'
            }),
            'avatar': forms.FileInput()
        }

# Update Nurse Form
class Update_Nurse_Form(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = [ 'first_name', 'last_name', 'email', 'phone_number', 'gender', 'nin', 'avatar' ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'class': 'form-control form-control-user'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'class': 'form-control form-control-user'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email Address',
                'class': 'form-control form-control-user'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Phone Number',
                'class': 'form-control form-control-user'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'nin': forms.TextInput(attrs={
                'placeholder': 'National Identity Number',
                'class': 'form-control form-control-user'
            }),
            'avatar': forms.FileInput()
        }

# Caretaker Form
class Caretaker_Form(forms.ModelForm):
    class Meta:
        model = Caretaker
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'class': 'form-control form-control-user'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'class': 'form-control form-control-user'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email Address',
                'class': 'form-control form-control-user'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Phone Number',
                'class': 'form-control form-control-user'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'nin': forms.TextInput(attrs={
                'placeholder': 'National Identity Number',
                'class': 'form-control form-control-user'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password',
                'class': 'form-control form-control-user'
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Repeat Password',
                'class': 'form-control form-control-user'
            }),
            'avatar': forms.FileInput()
        }

# Update Caretaker Form
class Update_Caretaker_Form(forms.ModelForm):
    class Meta:
        model = Caretaker
        fields = [ 'first_name', 'last_name', 'email', 'phone_number', 'gender', 'nin', 'avatar' ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'class': 'form-control form-control-user'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'class': 'form-control form-control-user'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email Address',
                'class': 'form-control form-control-user'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Phone Number',
                'class': 'form-control form-control-user'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'nin': forms.TextInput(attrs={
                'placeholder': 'National Identity Number',
                'class': 'form-control form-control-user'
            }),
            'avatar': forms.FileInput()
        }

# Patient Form
class Patient_Form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'class': 'form-control form-control-user'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'class': 'form-control form-control-user'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Phone Number',
                'class': 'form-control form-control-user'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'nin': forms.TextInput(attrs={
                'placeholder': 'National Identity Number',
                'class': 'form-control form-control-user'
            }),
            'weight': forms.TextInput(attrs={
                'placeholder': 'Weight',
                'class': 'form-control form-control-user'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password',
                'class': 'form-control form-control-user'
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Repeat Password',
                'class': 'form-control form-control-user'
            }),
            'avatar': forms.FileInput()
        }

# Update Patient Form
class Update_Patient_Form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [ 'first_name', 'last_name', 'phone_number', 'gender', 'nin', 'weight', 'avatar' ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'class': 'form-control form-control-user'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'class': 'form-control form-control-user'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Phone Number',
                'class': 'form-control form-control-user'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'nin': forms.TextInput(attrs={
                'placeholder': 'National Identity Number',
                'class': 'form-control form-control-user'
            }),
            'weight': forms.TextInput(attrs={
                'placeholder': 'Weight',
                'class': 'form-control form-control-user'
            }),
            'avatar': forms.FileInput()
        }


