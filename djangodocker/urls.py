from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangodocker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^celery/$', 'djangodocker.views.add_celery_task'),

    url(r'^admin/', include(admin.site.urls)),
)
