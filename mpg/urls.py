import django
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from mpg import settings

urlpatterns = [
    url(r'^', include('lpage.urls')),
    url(r'^admin', admin.site.urls),
]

urlpatterns += [
    # 'django.views.static',
    # url(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += [
    url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),
]
