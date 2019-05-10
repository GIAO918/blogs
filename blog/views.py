from django.shortcuts import render, HttpResponse
from .models import Tag, Post, Category
from django import forms
from django.forms import widgets
from blog import models
from django.core.validators import RegexValidator, ValidationError  # 用于forms正则校验

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


# def post_detail(request, post_id):
# try:
#     post = Post.objects.get(id=post_id)
# except Post.DoesNotExist:
#     post = None
# context = {
#     "post":post,
#     "siderbars": SideBar.get_all(),
# }
# context.update(Category.get_navs())
# return render(request, "detail.html", context = context)
from django.views.generic import DetailView, ListView


# class PostDetailView(DetailView):
#     model = Post
#     template_name = "detail.html"

class PostDetailView(DetailView):
    model = Post    # 获取哪一个model的单个对象
    template_name = "post_list.html"        # 渲染的模型
    pk_url_kwarg = 1

# Create your views here.

# class RegForm(forms.Form):
#     user = forms.CharField(label="用户名", min_length=6, max_length=16,
#                            error_messages={"required": "用户名不能为空",
#                                            "min_length": "用户名不能小于6位",
#                                            "max_length": "用户名长度不能超多16"},
#                            widget=widgets.TextInput(attrs={"class": "form-control"}))
#     email = forms.EmailField(label="邮箱",
#                              error_messages={"required": "邮箱不能为空",
#                                              "invalid": "请输入正确格式的邮箱"},
#                              widget=widgets.EmailInput(attrs={"class": "form-control"}))
#     phone = forms.CharField(label="手机号",
#                             # 用正则定制自定义校验规则
#                             validators=[
#                                 RegexValidator(r'^[0-9]+$', "手机号必须是数字"),
#                                 RegexValidator(r'^1[3-9][0-9]{9}$', "手机格式有误")
#                             ],
#                             widget=widgets.TextInput(attrs={"class": "form-control"}),
#                             error_messages={"required": "手机号不能为空"}
#                             )
#     pwd = forms.CharField(label="密码", min_length=6, max_length=16,
#                           error_messages={"required": "密码不能为空",
#                                           "min_length": "密码长度不能小于6"},
#                           widget=widgets.PasswordInput(attrs={"class": "form-control"}))
#     rpwd = forms.CharField(label="确认密码", min_length=6, max_length=16,
#                            error_messages={"required": "密码不能为空",
#                                            "min_length": "密码长度不能小于6"},
#                            widget=widgets.PasswordInput(attrs={"class": "form-control"}))
#
#     # 重写父类的clean方法
#     def clean(self):
#         # 通过校验的字段此时都保存在self.clean_data
#         pwd = self.cleaned_data.get("pwd")
#         rpwd = self.cleaned_data.get("rpwd")
#         if pwd != rpwd:
#             self.add_error("rpwd", ValidationError("两次的密码不一致"))
#             raise ValidationError("两次密码不一致")
#         return self.cleaned_data
#
#
# """
#     city = forms.fields.ChoiceField(
#         label="所在城市",
#         widget=widgets.RadioSelect
#     )
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["city"].choices = models.City.objects.all().values_list("id", "name")
# """
#
#
# def register(request):
#     reg_obj = RegForm()
#     if request.method == "POST":
#         reg_obj = RegForm(request.POST)
#         if reg_obj.is_valid():
#             ret = reg_obj.cleaned_data
#             models.UserInfo.objects.create(user=ret["user"], pwd=ret["pwd"], email=ret["email"], phone=ret["phone"], )
#             return HttpResponse("注册成功")
#         print(reg_obj.errors)
#     return render(request, "register.html", {"reg_obj": reg_obj})
