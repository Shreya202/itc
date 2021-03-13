from django import forms
from django.forms import ModelForm
from .models import Candidate, Panelist, PanelistSchedule, Interview
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = "__all__"
    SKILL_CHOICES = (
        ('JAVA','JAVA'),
        ('PYTHON','PYTHON'),
        ('FULL STACK','FULL STACK'),
        ('BACKEND','BACKEND'),
    )
    GRADE_CHOICES = (
        ('IS1','IS1'),
        ('IS2','IS2'),
        ('IS3','IS3'),
    )  
    SCREENING_CHOICES = (
        ('PENDING','PENDING'),
        ('WIP','WIP'),
        ('COMPLETE','COMPLETE'),
    )

    SELECTION_CHOICES = (
        ('SELECTED','SELECTED'),
        ('REJECTED','REJECTED')
    )
    widgets = {
            'Skill_Category': forms.Select(choices=SKILL_CHOICES,attrs={'class': 'form-control'}),
            'Grade': forms.Select(choices=GRADE_CHOICES,attrs={'class': 'form-control'}),
            'Screening_Phase': forms.Select(choices=SCREENING_CHOICES,attrs={'class': 'form-control'}),
            'Final_status': forms.Select(choices=SELECTION_CHOICES,attrs={'class': 'form-control'}),
        }
      
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class PanelistForm(ModelForm):
    class Meta:
        model = Panelist
        fields = "__all__"


class PanelistScheduleForm(ModelForm):
    class Meta:
        model = PanelistSchedule
        fields = "__all__"        
    widgets = {
            'Available_from': forms.DateTimeInput(attrs={'class': 'datetime-input','id': 'Available_from'}),
            'Available_till': forms.DateTimeInput(attrs={'class': 'datetime-input','id': 'Available_till'})
    }

class InterviewScheduleForm(ModelForm):
    class Meta:
        model = Interview
        fields = "__all__"    
        
    

