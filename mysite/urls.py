from django.conf.urls import patterns, include, url
from mysite.views import hello,current_datetime,hours_ahead,ua_display,search,contact
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^time/$',current_datetime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^display$',ua_display),
    # url(r'^search_form/$',search_form),
    url(r'^search/$',search),
    url(r'^contact/$',contact),
)
