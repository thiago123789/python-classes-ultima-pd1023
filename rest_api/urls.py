from django.urls import path

from rest_framework.routers import SimpleRouter

from rest_api.views import hello_world, ReservaModelViewSet, PetshopModelViewSet

app_name = 'rest_api'

router = SimpleRouter(trailing_slash=True)
router.register('reserva', ReservaModelViewSet)
router.register('petshop', PetshopModelViewSet)

## /api/reserva

urlpatterns = [
    path('hello', hello_world, name='hello_world_api')
]

urlpatterns += router.urls
