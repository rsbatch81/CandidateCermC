from django.conf.urls import url, include
from rest_framework import routers
from heatmap import views

router = routers.DefaultRouter()
router.register(r'addresses', views.ipv6AddressViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.MapView.as_view(), name='heatmap'),
]