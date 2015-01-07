from django.conf.urls import patterns, include, url
from blog import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^ueditor/',include('DjangoUeditor.urls' )),
    url(r'^admin/', include(admin.site.urls)),
    (r'^base/$', views.r_sidebar),
    (r'^blog/$', views.default),
)
