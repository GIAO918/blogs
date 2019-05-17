from django.conf.urls import url
from django.contrib import admin

from blog.views import (IndexView,CategoryView,TagView,PostDetailView)
from .custom_site import custom_site

from blog.views import MyView
urlpatterns = [
    url(r"^test/(?P<pk>\d+)$",MyView.as_view()),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name="category-list"),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name="tag-list"),

    url(r"^post/(?P<pk>\d+)", PostDetailView.as_view(), name='post-detail'),
    # url(r'^links/$', views.link，name = "link),
    url(r'admin/', custom_site.urls, name="admin"),
    url(r"^super_admin/", admin.site.urls, name="super-admin"),

]
