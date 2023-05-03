from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Retype Password'

class StudentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = "Student's Name"
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['placeholder'] = "Student's Phone"
        self.fields['registration_number'].widget.attrs['class'] = 'form-control'
        self.fields['registration_number'].widget.attrs['placeholder'] = "registration_number"
        self.fields['dept'].widget.attrs['class'] = 'form-control'
        self.fields['dept'].widget.attrs['placeholder'] = 'Department'
        self.fields['level'].widget.attrs['class'] = 'form-control'
        self.fields['level'].widget.attrs['placeholder'] = 'Level'
        self.fields['dob'].widget.attrs['class'] = 'form-control'
        self.fields['dob'].widget.attrs['placeholder'] = 'Date of Birth in format yyyy-mm-dd'
        self.fields['pob'].widget.attrs['class'] = 'form-control'
        self.fields['pob'].widget.attrs['placeholder'] = 'Place of Birth'
        # self.fields['profile_pic'].widget.attrs['class'] = 'file-upload-default'
        # self.fields['profile_pic'].widget.attrs['class'] = 'form-control file-upload-info'
        # self.fields['profile_pic'].widget.attrs['disabled placeholder'] = "Upload Image"

    class Meta:
        model = Student
        fields = ['name','phone','registration_number','dept','level','dob','pob','profile_pic',]



class AdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdminForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = "Admin's Name"
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['placeholder'] = "Admin's Phone"
        # self.fields['profile_pic'].widget.attrs['class'] = 'file-upload-default'
        # self.fields['profile_pic'].widget.attrs['class'] = 'form-control file-upload-info'
        # self.fields['profile_pic'].widget.attrs['disabled placeholder'] = "Upload Image"
        
    class Meta:
        model = AdminUser
        fields = ['name','phone','profile_pic',]

# class Myform(forms.Form):
#     course_code = forms.CharField(max_length=200)
#     registration_number = forms.CharField(max_length=200)

class UpdateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        #self.fields['student'].widget.attrs['class'] = 'form-control'
        self.fields['student'].widget.attrs['hidden'] = True
        #self.fields['course_code'].widget.attrs['class'] = 'form-control'
        self.fields['course_code'].widget.attrs['hidden'] = True
        self.fields['theory_marks'].widget.attrs['class'] = 'form-control'
        self.fields['term_test'].widget.attrs['class'] = 'form-control'
        #self.fields['total'].widget.attrs['class'] = 'form-control'
        self.fields['total'].widget.attrs['hidden'] = True
        #self.fields['dept'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = Result
        fields ='__all__'


class AddResultForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddResultForm, self).__init__(*args, **kwargs)
        self.fields['student'].widget.attrs['hidden'] = True
        self.fields['course_code'].widget.attrs['class'] = 'form-control'
        self.fields['course_code'].widget.attrs['hidden'] = True
        self.fields['marks'].widget.attrs['class'] = 'form-control'
        self.fields['attendence'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = Result
        fields = '__all__'


class AddSubjectForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddSubjectForm, self).__init__(*args, **kwargs)
        self.fields['course_code'].widget.attrs['class'] = 'form-control'
        self.fields['course_code'].widget.attrs['placeholder'] = "Course Code"
        self.fields['subject_name'].widget.attrs['class'] = 'form-control'
        self.fields['subject_name'].widget.attrs['placeholder'] = "Subject's Name"
        self.fields['credit'].widget.attrs['class'] = 'form-control'
        self.fields['credit'].widget.attrs['placeholder'] = "Credit"
        self.fields['subtype'].widget.attrs['class'] = 'form-control'
        self.fields['subtype'].widget.attrs['placeholder'] = "Genre"
        self.fields['level'].widget.attrs['class'] = 'form-control'
        self.fields['level'].widget.attrs['placeholder'] = "Level"
        self.fields['semester'].widget.attrs['class'] = 'form-control'
        self.fields['semester'].widget.attrs['placeholder'] = "Semester"
        self.fields['dept'].widget.attrs['class'] = 'form-control'
        self.fields['dept'].widget.attrs['placeholder'] = "Department"
    class Meta:
        model = Subject
        fields = '__all__'
    

class TeacherForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = "Teachers's Name"
        self.fields['dept'].widget.attrs['class'] = 'form-control'
        self.fields['dept'].widget.attrs['placeholder'] = "Teacher's Dept"
        self.fields['teacher_id'].widget.attrs['class'] = 'form-control'
        self.fields['teacher_id'].widget.attrs['placeholder'] = "Teachers's ID"
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['placeholder'] = "Teacher's Phone"


    class Meta:
        model = Teacher
        fields = ['name','dept','teacher_id','phone','profile_pic',]


class DepartmentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        self.fields['school'].widget.attrs['class'] = 'form-control'
        self.fields['school'].widget.attrs['placeholder'] = "School to which the Department Belongs"
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = "Department Name"
        self.fields['dept_id'].widget.attrs['class'] = 'form-control'
        self.fields['dept_id'].widget.attrs['placeholder'] = "Department ID"
    class Meta:
        model = Dept
        fields = ['school','name','dept_id',]

class SchoolForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SchoolForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = "School Name"
        self.fields['school_id'].widget.attrs['class'] = 'form-control'
        self.fields['school_id'].widget.attrs['placeholder'] = "School ID"
    class Meta:
        model = School
        fields = ['name','school_id',]

class DegreeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DegreeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = "Degree Name"
        self.fields['deg_id'].widget.attrs['class'] = 'form-control'
        self.fields['deg_id'].widget.attrs['placeholder'] = "Degree ID"
        self.fields['total_credits'].widget.attrs['class'] = 'form-control'
        self.fields['total_credits'].widget.attrs['placeholder'] = "Total Number of credits required to complete degree"
    class Meta:
        model = Degree
        fields = '__all__'

class SSForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SSForm, self).__init__(*args, **kwargs)
        self.fields['session'].widget.attrs['class'] = 'form-control'
        self.fields['session'].widget.attrs['placeholder'] = "Session  e.g 2022/2023"
        self.fields['semester'].widget.attrs['class'] = 'form-control'
        self.fields['semester'].widget.attrs['placeholder'] = "Semester"
        self.fields['ss_id'].widget.attrs['class'] = 'form-control'
        self.fields['ss_id'].widget.attrs['placeholder'] = "Semester ID e.g S1/22/23 for Semester 1 of 2022/2023 Session"
        self.fields['semester_start'].widget.attrs['class'] = 'form-control'
        self.fields['semester_start'].widget.attrs['placeholder'] = "Semester Start  in format yyyy-mm-dd"
        self.fields['semester_end'].widget.attrs['class'] = 'form-control'
        self.fields['semester_end'].widget.attrs['placeholder'] = "Semester End  in format yyyy-mm-dd"
        self.fields['ca_deadline'].widget.attrs['class'] = 'form-control'
        self.fields['ca_deadline'].widget.attrs['placeholder'] = "Deadline for teachers to submit CAs in format yyyy-mm-dd"
    class Meta:
        model = SemesterSession
        fields = ['session','semester','ss_id','semester_start','semester_end','ca_deadline']

    




