from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from user.views import UserAPI, LoginAPI, LogoutAPI

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register(r'user', UserAPI)

urlpatterns += [
    url('', include(router.urls)),
    path('login/', LoginAPI.as_view(), name='user-login'),
    path('logout/', LogoutAPI.as_view(), name='user-logout')
]