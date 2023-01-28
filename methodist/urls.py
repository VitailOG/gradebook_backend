from rest_framework import routers

from methodist.api.endpoints import DV, PV

router = routers.SimpleRouter()

router.register('dv', DV, basename='dv')

router.register('ps', PV, basename='ps')

urlpatterns = []

urlpatterns += router.urls
