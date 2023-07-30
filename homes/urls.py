from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('tenants', views.TenantViewSet)
router.register('property', views.PropertyViewSet)
router.register('flat', views.FlatViewSet)
router.register('lease', views.LeaseViewSet)


urlpatterns = router.urls
