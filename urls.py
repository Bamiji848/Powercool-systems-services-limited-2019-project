
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import include, url
from powercool_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from powercool_app.sitemaps import Static_Sitemap
from django.views.generic.base import TemplateView

sitemaps = {
    'static': Static_Sitemap(),
}


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('blog/', views.blog, name='blog'),
    path('profile_view/', views.profile_view, name='profile_view'),
    path('products/', views.products, name='products'),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="powercool_app/robots.txt", content_type="text/plain"),
    ),
    path('contact/', views.contact, name='contact'),
    path('<int:id>/', views.blog_single, name='blog_single'),
    path('service_detail/<int:id>/', views.service_detail, name='service_detail'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('products_detail/<int:id>/', views.products_detail, name='products_detail'),
    path('powercool_app', include('powercool_app.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


