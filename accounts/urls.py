from django.urls import re_path
from rest_framework import routers

from accounts.views import GetUserKeyPassword, UserViewset

router = routers.SimpleRouter()

router.register(r'users', UserViewset, basename='UserModel')

urlpatterns = [
    re_path('get-user-key-password/', GetUserKeyPassword.as_view(), name='get-user-key-password'),    
]

urlpatterns += router.urls