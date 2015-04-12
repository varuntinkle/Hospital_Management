from django.conf.urls import patterns,include,url
from django.views.generic import ListView, DetailView
from database.models import Post
import datetime
from datetime import date 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=patterns('',
                     url(r'^$',ListView.as_view(
                         queryset=Post.objects.all().order_by("-date")[:1000],
                         template_name="blog.html")),


                    url(r'^(?P<pk>\d+)$',DetailView.as_view(
                         model=Post,
                         template_name="post.html")),

                


)

urlpatterns += staticfiles_urlpatterns()
