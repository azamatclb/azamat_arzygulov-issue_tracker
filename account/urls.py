from django.urls import path

from account.views import login_view, logout_view, RegisterView

app_name = 'account'

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name='logout'),
    path('registration/', RegisterView.as_view(), name='registration')

]
