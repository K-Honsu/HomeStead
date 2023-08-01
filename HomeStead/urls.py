from . import docs
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homes/', include('homes.urls')),
    # path('docs/', include('HomeStead.docs')),
    path('docs/', include(docs))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)