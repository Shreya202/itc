from django.db import models
from django.utils import timezone



class Candidate(models.Model):
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
    
    Candidate_Name = models.CharField(max_length=70)
    Skill_Category = models.CharField(max_length=20,choices = SKILL_CHOICES)
    Account = models.CharField(max_length = 50)
    Grade = models.CharField(max_length=10,choices = GRADE_CHOICES)
    Role = models.CharField(max_length=20)
    Billing_Date = models.DateField()
    OnBoard_Date = models.DateField(default='2021-01-01')
    Screening_Phase = models.CharField(max_length=20,choices = SCREENING_CHOICES)
    Final_status = models.CharField(max_length = 10, choices = SELECTION_CHOICES,default = 'SELECTED')

    def __str__(self):
        return self.Candidate_Name

class Panelist(models.Model):
   
    Psid = models.IntegerField()
    First_name = models.CharField(max_length = 70)
    Last_name = models.CharField(max_length = 70)
    Skill = models.CharField(max_length = 30,null = True)

    def __str__(self):
        return self.First_name
    

class Recruiter(models.Model):
    
    Psid = models.IntegerField()
    First_name = models.CharField(max_length = 70)
    Last_name = models.CharField(max_length = 70)

class PanelistSchedule(models.Model):
    Panelname = models.ForeignKey(Panelist, on_delete = models.CASCADE)    
    Available_from = models.DateTimeField()
    Available_till = models.DateTimeField()

    def __str__(self):
        return (str(self.Panelname) + ' Schedule')

class Interview(models.Model):
    Candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE)
    Panel = models.ForeignKey(Panelist, on_delete = models.CASCADE)
    Interview_time = models.DateTimeField() 

    def __str__(self):
        return (str(self.Candidate) + ' Interview')