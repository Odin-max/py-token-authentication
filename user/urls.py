from django.urls import path
from .views import RegisterView, CustomAuthToken, ManageUserView

app_name = "users"

urlpatterns = [
    path("api/user/register/", RegisterView.as_view(), name="user-register"),
    path("api/user/login/", CustomAuthToken.as_view(), name="user-login"),
    path("api/user/me/", ManageUserView.as_view(), name="user-me"),
]

