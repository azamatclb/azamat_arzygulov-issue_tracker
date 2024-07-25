from django.urls import path

from account.views import index

app_name = 'account'

urlpatterns = [
    path('', index)
]
