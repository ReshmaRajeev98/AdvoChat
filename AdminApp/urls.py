from django.urls import path
from .import views

urlpatterns = [
    path('',views.Admin, name='Admin'),
    path("AddLaw",views.AddLaw, name='AddLaw'),
    path("getLaw",views.getLaw, name='getLaw'),
    path('ViewLaw', views.ViewLaw, name='ViewLaw'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('edit/<int:eid>/', views.edit, name='edit'),
    path('UpdateLaw/<int:id>/',views.UpdateLaw,name='UpdateLaw'),
    path('ViewLawyerReq', views.ViewLawyerReq, name='ViewLawyerReq'),
    path('AcceptLawyerReq/<int:LRAid>/', views.AcceptLawyerReq, name='AcceptLawyerReq'),
    path('RejectLawyerReq/<int:LRDid>/', views.RejectLawyerReq, name='RejectLawyerReq'),
    path('ViewLawyers', views.ViewLawyers, name='ViewLawyers'),
    path('ViewUserReq', views.ViewUserReq, name='ViewUserReq'),
    path('AcceptUserReq/<int:UAid>/', views.AcceptUserReq, name='AcceptUserReq'),
    path('RejectUserReq/<int:UDid>/', views.RejectUserReq, name='RejectUserReq'),
    path('ViewCases', views.ViewCases, name='ViewCases'),
    path('ViewUsers', views.ViewUsers, name='ViewUsers')
]