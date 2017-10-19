from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('lpage.urls')),
    url(r'^admin', admin.site.urls),
]

urlpatterns += [
    # 'django.views.static',
    # url(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
]
