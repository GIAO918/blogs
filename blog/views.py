from django.shortcuts import render, HttpResponse
from .models import Tag, Post, Category
from django import forms
from django.forms import widgets
from blog import models

from config.models import SideBar

def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None
    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)

    elif category_id:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posts()
    context = {
        "category": category,
        "tag": tag,
        "post_list": post_list,
        "siderbars": SideBar.get_all(),
    }
    context.update(Category.get_navs())
    return render(request, 'list.html', context=context)



from django.views.generic import DetailView, ListView


class PostDetailView(DetailView):
    model = Post
    template_name = "detail.html"

