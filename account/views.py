from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from account.forms import UserRegisttrationForm

User = get_user_model()


# Create your views here.

def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_path = request.POST.get('next', 'webapp:project_list')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_path)
        else:
            context["has_error"] = True
    context['next_param'] = request.GET.get('next')
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('webapp:project_list')


class RegisterView(CreateView):
    template_name = 'registration.html'
    form_class = UserRegisttrationForm
    model = User

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        pass
