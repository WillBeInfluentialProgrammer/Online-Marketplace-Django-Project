from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from app import views


urlpatterns = [
    path('',views.index, name='index'),
    path('items/', include('item.urls')),
    path('contact/',views.contact, name='contact'),
    path('admin/', admin.site.urls),
]
if (settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

