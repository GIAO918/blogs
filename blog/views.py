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
        try:
            tag = Tag.objects.get(id=tag_id)  # 根据标签拿到标签对象
        except Tag.DoesNotExist:
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)  # 根据标签对象反向查询所有的文章
    else:
        post_list = Post.objects.filter(status=Post.STATUS_NORMAL)
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
            except category.DoesNotExist:
                category = None
            else:
                post_list = post_list.filter(category_id=category_id)

    context = {
        "category": category,
        "tag": tag,
        "post_list": post_list
    }
    return render(request, "blog/list.html", context=context)


def detail(request, post_id=None):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    return render(request, "blog/detail.html", context={"post": post})
