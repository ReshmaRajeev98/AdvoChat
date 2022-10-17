from django.urls import path
from .import views

urlpatterns = [
    path('User',views.User, name='User'),
    path("UserReg",views.UserReg, name='UserReg'),
    path("getDataUser",views.getDataUser,name='getDataUser'),
    path("Login",views.Login,name='Login'),
    path("LawyerReg",views.LawyerReg, name='LawyerReg'),
    path("getDataLawyer",views.getDataLawyer, name='getDataLawyer'),
    path("user_logout",views.user_logout,name='user_logout'),
    path("Laywer_logout",views.Laywer_logout,name='Laywer_logout'),
    path("FindLawyer/<str:name>/",views.FindLawyer,name='FindLawyer'),
    path("BookConsult",views.BookConsult,name='BookConsult'),
    path("getDataConsult",views.getDataConsult,name='getDataConsult'),
    path('Find',views.Find, name='Find'),
    path('ViewReq',views.ViewReq, name='ViewReq'),
    path('accept/<int:eid>/',views.accept, name='accept'),
    path('decline/<int:id>/',views.decline, name='decline'),
    path('ViewReqUser',views.ViewReqUser, name='ViewReqUser'),
    path('resubmit/<int:uid>/',views.resubmit, name='resubmit'),
    path("ContactUs",views.ContactUs,name='ContactUs'),
    path("getDataMsg",views.getDataMsg,name='getDataMsg')
]