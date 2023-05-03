from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from datetime import date, datetime

class School(models.Model):
    school_id = models.CharField(max_length= 10, null=False, primary_key=True)
    name = models.CharField(max_length= 200, null= True)
    def __str__(self):
        return self.name

class Degree(models.Model):
    deg_id = models.CharField(max_length=10, null= False, primary_key= True)
    name = models.CharField(max_length= 200, null= True)
    total_credits = models.IntegerField(null= False, default=60)   
    def __str__(self):
        return self.name

class SemesterSession(models.Model):
    session = models.CharField(max_length=9, null= False, blank= False)
    semester = models.CharField(max_length= 200, null = False, choices= [('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2') ])
    ss_id = models.CharField(max_length=9, null= False, primary_key = True)
    semester_start = models.DateField(null= False, default= datetime.now())
    semester_end = models.DateField(null= False, default= datetime.now())
    ca_deadline = models.DateField(null= False, default= datetime.now())
    active = models.BooleanField(null= True, blank=True, default= True)

    def __str__(self):
        return self.ss_id
class Dept(models.Model):
    school = models.ForeignKey(School, on_delete= models.CASCADE, default="")
    dept_id = models.CharField(max_length= 10, null=False, primary_key=True)
    name = models.CharField(max_length= 200, null= True)
    def __str__(self):
        return self.dept_id
    
class Student(models.Model):
    user = models.OneToOneField(User, null = True, on_delete= models.CASCADE)
    registration_number = models.CharField(max_length= 200, null=False, primary_key=True)
    degree_pursued = models.ForeignKey(Degree, on_delete= models.CASCADE, default="")
    dept = models.ForeignKey(Dept, on_delete= models.CASCADE)
    name = models.CharField(max_length= 200, null= True)
    phone = models.CharField(max_length= 200, null = True)
    profile_pic = models.ImageField(null = True, blank = True, default= '0000.jpeg')
    level = models.CharField(max_length= 200, null= True, choices= [('HND1', 'HND1'), ('HND2', 'HND2'), ('BTECH', 'BTECH')  ])
    dob = models.DateField(null = True, blank = True)
    pob = models.CharField(max_length= 200, null= True)
    
    def __str__(self):
        return self.registration_number

class AdminUser(models.Model):
    user = models.OneToOneField(User, null = True, on_delete= models.CASCADE)
    name = models.CharField(max_length= 200, null= True)
    phone = models.CharField(max_length= 200, null = True)
    profile_pic = models.ImageField(null = True, blank = True, default="0000.jpeg")

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(User, null = True, on_delete= models.CASCADE)
    name = models.CharField(max_length= 200, null= True)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length= 200, null=False, primary_key=True)
    phone = models.CharField(max_length= 200, null = True)
    profile_pic = models.ImageField(null = True, blank = True, default="0000.jpeg")

    def __str__(self):
        return self.name

class AssignedTeacher2(models.Model):
    student_dept = models.CharField(max_length= 3)
    dept = models.ForeignKey(Dept,on_delete=models.CASCADE)
    course_code = models.CharField(max_length= 200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("teacher","course_code"))

class Subject(models.Model):
    course_code = models.CharField(max_length= 200, primary_key= True)
    subject_name = models.CharField(max_length= 200)
    credit = models.FloatField(null = True)
    semester = models.CharField(max_length= 200, null = True, choices= [('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2') ])
    subtype = models.CharField(max_length= 200, null=True)
    dept =models.ForeignKey(Dept, on_delete=models.CASCADE)
    level = models.CharField(max_length= 200, null= True, choices= [('HND1', 'HND1'), ('HND2', 'HND2'), ('BTECH', 'BTECH') ])
    
class RegisterTable(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    status = models.CharField(max_length= 200, default= "Approved")
    dept =models.ForeignKey(Dept, on_delete=models.CASCADE)
    class Meta:
        unique_together = (("student","subject"))


class Result(models.Model):
    sem_ses = models.ForeignKey(SemesterSession, on_delete= models.CASCADE, default="")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_code = models.CharField(max_length= 200)
    theory_marks  = models.IntegerField(null = True)
    term_test  = models.IntegerField(null = True)
    total = models.FloatField(null = True)
    dept = models.CharField(max_length=3, null= True)
    class Meta:
        unique_together = (("student","course_code"))
    

class Rating(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    rating  = models.IntegerField(default = '3')
    class Meta:
        unique_together = (("student","subject"))








