from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Tag, Post, Category
from django.views.generic import DetailView, ListView
from config.models import SideBar
from django import forms
from django.forms import widgets
from blog import models

from config.models import SideBar


class IndexView(ListView):
    queryset = Post.latest_posts()  # 获取最新的文章对象
    paginate_by = 5
    context_object_name = "post_list"   # 要渲染到模板的queryset名称
    template_name = "blog/list.html"


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):   # 拿到渲染到模板的数据
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


# def post_list(request, category_id=None, tag_id=None):
#     tag = None
#     category = None
#
#     if tag_id:
#         post_list, tag = Post.get_by_tag(tag_id)
#     elif category_id:
#         post_list, category = Post.get_by_category(category_id)
#     else:
#         post_list = Post.latest_posts()
#     context = {
#         "category": category,
#         "tag": tag,
#         "post_list": post_list,
#         "sidebars": SideBar.get_all()
#     }
#     context.update(Category.get_navs())
#     return render(request, "blog/list.html", context=context)
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
# def post_detail(request, post_id=None):
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         post = None
#     context = {
#         "post": post,
#         "sidebars": SideBar.get_all(),
#     }
#     context.update(Category.get_navs())
#     return render(request, "blog/detail.html", context=context)
