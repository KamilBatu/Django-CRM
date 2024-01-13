from django.urls import path
from .views import home, logout_user, register

urlpatterns = [
    path('', home, name='home'),
    # path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register')

]
