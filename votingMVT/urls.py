from django.urls import path
from . import views
urlpatterns = [
        path('',views.index,name='index'),
        path('register',views.registration,name='register'),
        path('login',views.loginUser,name='login'),
        path('logout',views.signout,name='logout'),
        path('profile',views.profile,name='profile'),
        path('home',views.home,name='home'),
        path('forgotpassword',views.forgotpwd,name="forgotpassword"),
        path('adminregister',views.adminreg,name='adminregister'),
        path('adminhome',views.adminHome,name='adminHome'),
        path('addcandidate',views.addcandidate,name='addcandidate'),
        path('deletecandidate',views.delCandidate,name='deletecandidate')
    ]