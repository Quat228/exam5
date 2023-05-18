from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path('account/register/', views.UserCreateAPIView.as_view()),
    path('account/token/', obtain_auth_token),
    path('account/auth/', include('rest_framework.urls'))
]
