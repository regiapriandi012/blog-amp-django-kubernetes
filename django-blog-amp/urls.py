from django.contrib import admin
from django.urls import path, include, re_path
from webregi.views import AdsView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from webregi.sitemaps import PostSitemap
from django.views.static import serve

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django-blog-amp-app.urls')),
    path('ads.txt', AdsView.as_view()),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('summernote/', include('django_summernote.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

handler404 = "django-blog-amp-app.views.page_not_found_view"

"""if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""