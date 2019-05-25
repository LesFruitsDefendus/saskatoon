from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    url(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    url(r'^$', views.index, name='index'),

    url(
        r'^login$',
        auth_views.login,
        name='login'
    ),
    url(
        r'^password_reset/$',
        auth_views.password_reset,
        name='password_reset'
    ),
    url(
        r'^password_reset/done/$',
        auth_views.password_reset_done,
        name='password_reset_done'
    ),
    url(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        name='password_reset_confirm'
    ),
    url(
        r'^reset/done/$',
        auth_views.password_reset_complete,
        name='password_reset_complete'
    ),
    url(
        r'^calendar$',
        views.Calendar.as_view(),
        name='calendar'
    ),
    url(
        r'^jsoncal',
        views.JsonCalendar.as_view(),
        name='calendarJSON'
    ),
]
