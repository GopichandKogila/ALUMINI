from django.urls import path
from alumni import views 


urlpatterns=[
    path('',views.home,name="homepage"),
    path('login',views.login,name="loginpage"),
    path('logout',views.logout,name="logoutpage"),
    path('profile',views.profile,name="profiletpage"),
    path('register',views.register,name="registerpage"),
    path('delete/<int:rid>',views.delete,name="postpage"),
    path('update/<int:rid>',views.update,name="updatepage"),   
    path('display/<int:rid>',views.dedicated,name="displaypage"),
    path('about',views.about,name="aboutpage"),
    path('contact',views.contact,name="contactpage"),
    path('staff',views.staff,name="staffpage"),
]