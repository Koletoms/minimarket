from django.urls import path

from .views import UserLoginView, UserLogoutView, SingUpView

app_name = "user_app"


urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("singup/", SingUpView.as_view(), name="sign_up"),
]
