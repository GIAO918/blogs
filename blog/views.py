from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Tag, Post, Category
from django.views.generic import DetailView, ListView
from django.db.models import Q
from config.models import SideBar
from django import forms
from django.forms import widgets
from blog import models

from config.models import SideBar


class IndexView(ListView):
    queryset = Post.latest_posts()  # 获取最新的文章对象
    paginate_by = 5
    context_object_name = "post_list"  # 要渲染到模板的queryset名称
    template_name = "blog/list.html"



class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get("category_id")
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            "category": category
        })
        return context

    def get_queryset(self):
        """重写queryset，根据分类过滤"""
        queryset = super().get_queryset()
        category_id = self.kwargs.get("category_id")
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get("tag_id")
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            "tag": tag,
        })
        return context

    def get_queryset(self):
        """重写queryset，根据标签过滤"""
        queryset = super().get_queryset()
        tag_id = self.kwargs.get("tag_id")
        return queryset.filter(tag__id=tag_id)


class PostDetailView(DetailView):  # 类方法获取文章对象
    queryset = Post.latest_posts()
    template_name = "blog/detail.html"
    context_object_name = "post"
    pk_url_kwarg = "post_id"

https://blog.csdn.net/chen_jint/article/details/15505949