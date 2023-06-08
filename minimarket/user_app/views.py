from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from basket_app.models import BasketProduct
from .forms import SignUpForm
from .models import Profile

User = get_user_model()


class UserLoginView(LoginView):
    """
    Преставление для залогинивания пользователя.
    """
    template_name = 'user_app/login.html'
    next_page = '/'

    def post(self, request, *args, **kwargs):
        basket_products = BasketProduct.objects.filter(session_key=request.session.session_key)
        response = super().post(request, *args, **kwargs)
        new_session_key = request.session.session_key
        for basket_product in basket_products:
            basket_product.session_key = new_session_key
            basket_product.save()
        return response


class UserLogoutView(LogoutView):
    """
    Преставление для разлогинивания пользователя.
    """
    template_name = 'user_app/logout.html'
    next_page = '/'

    # def get(self, request, *args, **kwargs):
    #     logger.info(f"Пользователь {request.user.username} разлогинился")
    #     return super().get(request, *args, **kwargs)


class SingUpView(View):
    """
    Преставление для регистрации пользователя.
    """
    next_page = '/'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = SignUpForm()
        context = {
            "form": form
        }
        return render(request, "user_app/signup.html", context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_number = form.cleaned_data.get('phone_number')
            Profile.objects.create(
                user=user,
                phone_number=phone_number
            )

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # logger.info(f"Пользователь {username} прошел регистрацию.")

            user.groups.add(Group.objects.get(name='clients'))
            return redirect('/')
