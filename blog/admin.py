from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Tag, Category, Post
from .adminforms import PostAdminForm
from blogs.custom_site import custom_site
from blogs.base_admin import BaseOwnerAdmin

class PostInline(admin.TabularInline):
    fields = ('title',"desc")
    extra = 1
    model = Post

@admin.register(Category,site = custom_site)  # 分类管理后台
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline,]
    list_display = ("name", "status", "is_nav", "created_time",)  # 修改的时候展示的参数
    fields = ("name", "status", "is_nav",)  # 后台添加要填的参数

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)

    # post_count.short_description = "文章数量"

@admin.register(Tag,site = custom_site)
class TagAdmin(BaseOwnerAdmin):  # 标签管理后台
    list_display = ("name", "status", "created_time")
    fields = ("name", "status",)

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(TagAdmin, self).save_model(request, obj, form, change)


# 侧边栏的过滤器只看到自己的分类
class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器 只展示当前用户分类"""
    title = "分类过滤器"
    parameter_name = "owner__category"

    def lookups(self, request, model_admin):  # 返回要展示的内容和查询ID
        return Category.objects.filter(owner=request.user).values_list("id", "name")

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post,site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        "title", "category", "status", "created_time", "operator", "owner"
    ]
    list_display_links = []
    list_filter = [CategoryOwnerFilter]  # 里边的字段决定列表页的过滤
    search_fields = ["title", "category_name"]
    actions_on_top = True
    actions_on_bottom = True
    exclude = ("owner",)
    save_on_top = True
    # fields = (
    #     ("category", "title"),
    #     "desc",
    #     "status",
    #     "content",
    #     "tag",
    # )

    filter_horizontal = ("tag",)  # 添加样式左右展示
    # filter_vertical = ("tag",)  # 添加样式上下展示

    # 添加页面布局的添加文章页面
    fieldsets = (
        ("基础配置", {
            "description": "基础配置描述",
            "fields": (("title", "category"),
                       "status",
                       )
        }),
        ("内容", {
            "fields": (
                "desc",
                "content",
            )
        }),
        ("额外信息", {
            "classes": ("collapse"),
            "fields": ("tag",),
        })
    )

    def operator(self, obj):
        return format_html(
            "<a href = '{}'>编辑</a>",
            reverse("cus_admin:blog_post_change", args=(obj.id,))
        )

    operator.short_description = "操作"

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(PostAdmin, self).save_model(request, obj, form, change)
    #
    # def get_queryset(self, request):  # 后台页面只显示自己的文章
    #     qs = super(PostAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)
    class Media:
        css = {
            "all":("https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css",)
        }
        js = ("https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js",)