'''定义learning_logs URL模式'''

from django.urls import path, include
from . import views

app_name = "users"
urlpatterns = [
    # 登录、注销 
    path('', include('django.contrib.auth.urls')),  
    # 注册
    path('register/', views.register, name='register'),  
]