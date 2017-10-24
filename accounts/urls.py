from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    url(r'^reset/$', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset.html',
        email_template_name='registration/password_reset_email.html',
    ), name='password_reset'),

    url(r'^reset/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),

    url(r'^settings/password-change/$', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change.html'), name='password_change'),
    url(r'^settings/password-change/done/$', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'),
        name='password_change_done'),
    # url(r'^Oauth/', include('social_django.urls', namespace='social')),
    # url('social-auth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^contact/?$', views.contact, name='contact'),

]
