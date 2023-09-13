from django.urls import path
from . import views

app_name = 'app_list'

urlpatterns = [
    path('index',views.index.as_view(), name = "index"),
    path('login/',views.loginPage,name="login"),
    path('',views.signup,name="signup"),
    path('logout/',views.LogoutPage,name="logout"),
]