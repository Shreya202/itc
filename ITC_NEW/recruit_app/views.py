from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from .forms import CandidateForm, CreateUserForm, PanelistForm, PanelistScheduleForm, InterviewScheduleForm
#from .forms1 import PanelistSignUpForm, RecruiterSignUpForm
from .models import Candidate, Panelist
from django.views.generic import CreateView
from .filters import CandidateFilter
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'recruit_app/dashboard.html')
@login_required(login_url = 'login')
def recruiter(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CandidateForm(request.POST)
        print("Correcr redirect")
        # check whether it's valid:
        if form.is_valid():
            print("start")


            form.save()
            print("Candidate saved")
            

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CandidateForm()

    return render(request,'recruit_app/recruiter.html',{'form': form})

@login_required(login_url = 'login')
def updatecandidate(request,id):
    updateemp = Candidate.objects.get(id = id)
    form = CandidateForm(request.POST,instance=updateemp)
    if form.is_valid():
        form.save()
        messages.success(request,"Record Updated Successfully..!")
        return redirect('search')
    else:
        messages.error(request,"No Update done")
            
    return render(request,'recruit_app/edit.html',{'editupdaterecord':updateemp})

               
@login_required(login_url = 'login')
def edit(request,id):
    display = Candidate.objects.get(id=id)
    print(display)
    return render(request,'recruit_app/edit.html',{'editupdaterecord':display})


@login_required(login_url = 'login')
def view(request):
    titles = Candidate.objects.all()
    context = {'title':titles}
    return render(request,'recruit_app/view.html',context)

@login_required(login_url = 'login')
def panelist(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PanelistForm(request.POST)
        print(form.errors)
        if form.is_valid():
            
            form.save()
            
            

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PanelistForm()
    return render(request,'recruit_app/panelist.html',{'form': form})     
@login_required(login_url = 'login')
def hr(request):
    return render(request,'recruit_app/hr.html')      

def register(request):
    return render(request,'recruit_app/register.html')

    template_name = '../templates/recruit_app/panelist_register.html'

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect ('/')

@login_required(login_url = 'login')
def search(request):
    candidate_list = Candidate.objects.all()
    candidate_filter = CandidateFilter(request.GET, queryset=candidate_list)
    return render(request, 'recruit_app/candidate_list.html', {'filter': candidate_filter})        

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('recruiter')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
        
            if form.is_valid():
                form.save()
            
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)
                return redirect('login')
        context = {'form':form}
        return render(request,'recruit_app/register.html',context)    
    

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('recruiter')
    else:    
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
        

            if user is not None:
                login(request,user)
                return redirect('recruiter')
            else:
                messages.info(request,'Username or Password is incorrect')    
            

        return render(request,'recruit_app/login.html')    
    

def logoutUser(request):
    logout(request)
    return redirect('login')    

@login_required(login_url = 'login')
def panelistschedule(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PanelistScheduleForm(request.POST)
        print(form.errors)
        if form.is_valid():
            
            form.save()
            
            

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PanelistScheduleForm()
    return render(request,'recruit_app/panelistschedule.html',{'form': form})

@login_required(login_url = 'login')
def interviewschedule(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InterviewScheduleForm(request.POST)
        print(form.errors)
        if form.is_valid():
            
            form.save()
            
            

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InterviewScheduleForm()
    return render(request,'recruit_app/interviewschedule.html',{'form': form})    


    



# Create your views here.
