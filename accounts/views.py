from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginView(View):
    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next')
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('website:index')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)

    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                login(request, user)
                if self.next:
                    return redirect(self.next)

            return redirect('website:index')
        messages.error(request, 'The information entered is incorrect')
        return render(request, 'accounts/login.html')


class LogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('website:index')


class SignUpView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('website:index')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('website:index')

        else:
            context = {'form': form}
            return render(request, 'accounts/signup.html', context)
