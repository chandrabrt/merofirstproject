from django.conf.urls import url
from blog import views
from blog.models import Post
from django.views.generic import UpdateView


app_name = 'blog'

urlpatterns = [
    # /blog/

    # url(r'^$', views.blog_index, name='blog_index'),
    url(r'^$', views.PostListView.as_view(), name='blog_index'),
    url(r'^about/$', views.about, name='about'),
    # url(r'^adminform/$', views.adminform, name='adminform'),
    url(r'^adminform/$', views.Adminform.as_view(), name='adminform'),
    url(r'^(?P<slug>[\w-]+)/update/$', views.MyUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.PostDeleteView.as_view(), name='post-delete'),
    url(r'^blog_contact/$', views.blog_contact, name='blog_contact'),
    # url(r'^success/$', views.success, name='success'),
    url(r'^nav/$', views.nav, name='nav'),
    url(r'^(?P<slug>[\w-]+)/$', views.blog_slug, name='blog_slug'),

   ]


