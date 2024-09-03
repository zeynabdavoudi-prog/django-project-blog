from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogView(View):
    def get(self, request, cat_name=None, author_username=None, tag_name=None):

        posts = Post.objects.filter(status=1).order_by('-published_date')
        posts_all = posts
        if cat_name:
            posts = posts.filter(category__name=cat_name)
        if author_username:
            posts = posts.filter(author__username=author_username)
        if tag_name:
            posts = posts.filter(tags__name__in=[tag_name])
        # pagination
        posts = Paginator(posts, 3)
        page_number = request.GET.get('page')
        try:
            posts = posts.get_page(page_number)
        except PageNotAnInteger:
            posts = posts.get_page(1)
        except EmptyPage:
            posts = posts.get_page(posts.num_pages)
        # section post category in html
        categories = Category.objects.all()
        cat_dict = {}
        for name in categories:
            cat_dict[name] = posts_all.filter(category=name).count()
        context = {'posts': posts,
                   'lasted_posts': posts_all[:min(4, len(posts_all))],
                   'cat_dict': cat_dict}
        return render(request, 'blog/blog-home.html', context)


class BlogSingleView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, status=1, id=post_id)
        # section latest posts
        posts = Post.objects.filter(status=1).order_by('-published_date')
        # comments post
        comments = Comment.objects.filter(post=post, approved=True)
        # show form
        form = CommentForm()
        # section post category in html
        cat_dict = {}
        categories = Category.objects.all()
        for name in categories:
            cat_dict[name] = posts.filter(category=name).count()
        context = {'post': post,
                   'lasted_posts': posts[:min(4, len(posts))],
                   'cat_dict': cat_dict,
                   'comments': comments,
                   'form': form}
        return render(request, 'blog/blog-single.html', context)

    def post(self, request, post_id):
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, status=1, id=post_id)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'your comment submitted successfully')
        else:
            messages.error(request, 'your comment didnt submitted ')
        return redirect('blog:blog_single', post_id)


class BlogSearchView(View):
    def get(self, request):
        search = request.GET.get('search')
        posts = Post.objects.filter(status=1, content__contains=search)
        # section post category in html
        cat_dict = {}
        categories = Category.objects.all()
        for name in categories:
            cat_dict[name] = Post.objects.filter(status=1, category=name).count()
        context = {'posts': posts,
                   'cat_dict': cat_dict}
        return render(request, 'blog/blog-home.html', context)
