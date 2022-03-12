from django.db import models


##########  Models  #########

# Gender models
class Gender:
    FEMALE = "Female"
    MALE = "Male"
    OTHER = "Other"

    CHOICES = (
        (MALE, MALE),
        (FEMALE, FEMALE),
        (OTHER, OTHER)
    )

# Doctor model.
class Doctor(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    nin = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=Gender.CHOICES)
    avatar = models.ImageField(upload_to="profile_image/doctor")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Doctor'

# Nurse model.
class Nurse(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    nin = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, default=Gender.MALE, choices=Gender.CHOICES)
    avatar = models.ImageField(upload_to="profile_image/nurse")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Nurse'

# Caretaker model.
class Caretaker(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    nin = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, default=Gender.MALE, choices=Gender.CHOICES)
    avatar = models.ImageField(upload_to="profile_image/caretaker")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Caretaker'

# Patient model
class Patient(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, null=True, blank=True)
    caretaker = models.ForeignKey(Caretaker, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    nin = models.CharField(max_length=100)
    weight = models.CharField(max_length=100, default=50)
    gender = models.CharField(max_length=6, default=Gender.MALE, choices=Gender.CHOICES)
    avatar = models.ImageField(upload_to="profile_image/patient")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Patient'


