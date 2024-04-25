from django.urls import path
from user_app.views import *

urlpatterns = [
    path('signup/',Signup.as_view(), name='Signup'),
    path('team/lead/signup/',TeamleadSignup.as_view(), name='Signup'),
    path('login/',Login.as_view(), name='login'),
    path('testview/',TestView.as_view(), name='testview'),
    path('logout/',Logout.as_view(), name='logout'),
]
