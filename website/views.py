from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from django.contrib import messages
from blog.models import *


class IndexView(View):
    def get(self, request):
        posts = Post.objects.filter(status=1)
        latest_posts = posts[0:min(6, posts.count())]
        context = {'latest_posts': latest_posts}
        return render(request, 'website/index.html', context)


class AboutView(View):
    def get(self, request):
        return render(request, 'website/about.html')


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        context = {'form': form}
        return render(request, 'website/contact.html', context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your ticket submitted successfully')
        else:
            messages.ERROR(request, 'your ticket didnt submitted ')

        return render(request, 'website/contact.html')


class NewsLetterView(View):
    def post(self, request):
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
        referer = request.META.get('HTTP_REFERER')
        return redirect(referer)
