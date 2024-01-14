from django.urls import path
from .views import home, logout_user, register, record_customer, delete_record, addRecord, update

urlpatterns = [
    path('', home, name='home'),
    # path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('record/<int:pk>/', record_customer, name='record'),
    path('delete/<int:pk>/', delete_record, name='delete'),
    path('update/<int:pk>/', update, name='update'),
    path('addRecord/', addRecord, name='addRecord')
]
