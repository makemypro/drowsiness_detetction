from django.urls import path, include
from knox import views as knox_views

from .views import DriverAPIView, UserDetailAPI, RegisterUserAPIView, DistanceMatrixAPIView, LoginAPI

urlpatterns = [
    path('', DriverAPIView.as_view(), name='drowsiness_detection'),
    path('distance-api', DistanceMatrixAPIView.as_view(), name='distance-api'),
    path("get-details", UserDetailAPI.as_view(), name='get-details'),
    path('register', RegisterUserAPIView.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path(r'api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]