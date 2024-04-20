
from django.db import models
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

class AcademicYear(models.Model):
    ay = models.CharField(max_length=10)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.ay
    
class SemesterSession(models.Model):
    session = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, default='')
    semester = models.CharField(max_length= 200, null = False, choices= [('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2') ])
    ss_id = models.CharField(max_length=9, null= False, primary_key = True)
    semester_start = models.DateField(null= False, default= datetime.now())
    semester_end = models.DateField(null= False, default= datetime.now())
    ca_deadline = models.DateField(null= False, default= datetime.now())
    ca_deadline_btech = models.DateField(null= False, default= datetime.now())
    ca_deadline_masters = models.DateField(null= False, default= datetime.now())
    result_deadline = models.DateField(null= False, default= datetime.now())
    result_deadline_btech = models.DateField(null= False, default= datetime.now())
    result_deadline_masters = models.DateField(null= False, default= datetime.now())
    active = models.CharField(max_length=3, null= False , choices=[('Yes', 'Yes'), ('No','No')], default= 'No')
    results_published = models.CharField(max_length=3, null= False , choices=[('Yes', 'Yes'), ('No','No')], default= 'No')

    def __str__(self):
        return self.ss_id
    
class Dept(models.Model):
    school = models.ForeignKey(School, on_delete= models.CASCADE, default="")
    dept_id = models.CharField(max_length= 10, null=False, primary_key=True)
    name = models.CharField(max_length= 200, null= True)
    UBa_Mentor_School = models.CharField(max_length = 200, null = True, choices= [('Faculty of Economics and Management Sciences (FEMS)', 'FEMS'), ('College of Technology (COLTECH)', 'COLTECH'), ('Faculty of Education (FED)', 'FED'), ('Higher Institute of Transport and Logistics (HITL)', 'HITL')],default = "Faculty of Economics and Management Sciences (FEMS)")
    def __str__(self):
        return self.dept_id
    
class Student(models.Model):
    user = models.OneToOneField(User, null = True, on_delete= models.CASCADE)
    registration_number = models.CharField(max_length= 200, null=False, primary_key=True)
    degree_pursued = models.ForeignKey(Degree, on_delete= models.CASCADE, default="")
    dept = models.ForeignKey(Dept, on_delete= models.CASCADE)
    name = models.CharField(max_length= 200, null= True)
    phone = models.CharField(max_length= 200, null = True)
    profile_pic = models.ImageField(null = True, blank = True, default= 'profile.jpg')
    level = models.CharField(max_length= 200, null= True, choices= [('HND1', 'HND1'), ('HND2', 'HND2'), ('BTECH', 'BTECH'), ('M1', 'M1'), ('M2', 'M2')])
    dob = models.DateField(null = True, blank = True)
    pob = models.CharField(max_length= 200, null= True)
    
    def __str__(self):
        return self.registration_number

class AdminUser(models.Model):
    user = models.OneToOneField(User, null = True, on_delete= models.CASCADE)
    name = models.CharField(max_length= 200, null= True)
    phone = models.CharField(max_length= 200, null = True)
    profile_pic = models.ImageField(null = True, blank = True, default="profile.jpg")

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(User, null = True, on_delete= models.CASCADE)
    name = models.CharField(max_length= 200, null= True)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length= 200, null=False, primary_key=True)
    phone = models.CharField(max_length= 200, null = True)
    profile_pic = models.ImageField(null = True, blank = True, default="profile.jpg")

    def __str__(self):
        return self.name
    
class Subject(models.Model):
    course_code = models.CharField(max_length= 200, primary_key= True)
    subject_name = models.CharField(max_length= 200)
    credit = models.FloatField(null = True)
    semester = models.CharField(max_length= 200, null = True, choices= [('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2') ])
    subtype = models.CharField(max_length= 200, null=True, choices= [('HND','HND'), ('DEGREE','DEGREE'), ('MASTER','MASTER')], default="HND" )
    dept = models.ManyToManyField(Dept, blank= True)
    dep = models.CharField(max_length= 200, null=True, blank = True)
    level = models.CharField(max_length= 200, null= True, choices= [('HND1', 'HND1'), ('HND2', 'HND2'), ('BTECH', 'BTECH'), ('M1', 'M1'), ('M2', 'M2') ])

    def __str__(self):
        return self.subject_name

    def save(self, *args, **kwargs):
        if not self.dept.all():
            self.dep = " "
        else:
            self.dep = str(self.dept.all()[0])
        super(Subject, self).save(*args, **kwargs)

class AssignedTeacher2(models.Model):
    dept = models.ForeignKey(Dept,on_delete=models.CASCADE)
    course = models.ForeignKey(Subject, on_delete=models.CASCADE, default="")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.teacher) + " - " + str(self.course)
    class Meta:
        unique_together = (("teacher","course"))

class RegisterTable(models.Model):
    sem_ses = models.ForeignKey(SemesterSession, on_delete=models.CASCADE, default= "S1/22/23")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    status = models.CharField(max_length= 200, default= "Approved")
    dept =models.ForeignKey(Dept, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student) + " - " + str(self.subject) + " - " + str(self.sem_ses.ss_id)
    class Meta:
        unique_together = (("student","subject","sem_ses"))


class Result(models.Model):
    sem_ses = models.ForeignKey(SemesterSession, on_delete= models.CASCADE, default="")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    level = models.CharField(max_length= 10, null = True, default= 'HND1')
    course_code = models.ForeignKey(Subject, on_delete=models.CASCADE, default="")
    theory_marks  = models.IntegerField(null = True, default = 0)
    term_test  = models.IntegerField(null = True, default= 0)
    term_test_resit  = models.IntegerField(null = True, default= 0)
    total = models.FloatField(null = True, default= 0)
    total_resit = models.FloatField(null = True, default= 0)
    dept = models.CharField(max_length=3, null= True)
    resited = models.CharField(max_length=3, null= False , choices=[('Yes', 'Yes'), ('No','No')], default= 'No')
    absent = models.CharField(max_length=3, null= False , choices=[('Yes', 'Yes'), ('No','No')], default= 'No')

    def save(self, *args, **kwargs):
        self.total = (int(self.theory_marks) + int(self.term_test))/5
        self.total_resit = (int(self.theory_marks) + int(self.term_test_resit))/5
        super(Result, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.student) + " - " + str(self.course_code) + " - " + str(self.sem_ses)
    class Meta:
        unique_together = (("student","course_code","sem_ses"))
    

class Rating(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    rating  = models.IntegerField(default = '3')
    def __str__(self):
        return str(self.student) + " - " + str(self.teacher) + " - " + str(self.subject)
    class Meta:
        unique_together = (("student","subject"))

class ExamCode(models.Model):
    sem_ses = models.ForeignKey(SemesterSession, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete= models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    code = models.IntegerField()

    class Meta:
        unique_together = (("sem_ses","subject","student"))

class Image(models.Model):
    title = models.CharField(null=True, max_length=200)
    pic = models.ImageField(null=True)







