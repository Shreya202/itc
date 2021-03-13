from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = "home"),
    path('recruiter/',views.recruiter,name = 'recruiter'),
    path('logout/',views.logoutUser,name = 'logout'),
    path('recruiter/interview',views.interviewschedule,name = 'interview'),
    path('recruiter/view/',views.view,name = 'view'),
    path('recruiter/search/',views.search,name = 'search'),
    path('recruiter/search/edit/<int:id>',views.edit ,name = 'edit'),
    path('recruiter/search/edit/update/<int:id>',views.updatecandidate,name = 'update'),
    path('panelist/',views.panelist,name = 'panelist'),
    path('panelist/schedule',views.panelistschedule,name = 'panelistschedule'),
    path('register/',views.registerPage,name = 'register'),
    path('login/',views.loginPage,name = 'login'),
    path('hr/',views.hr,name = 'hr'),
]