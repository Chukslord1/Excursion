from excursionapp.viewsets import ExcursionViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('excursion',ExcursionViewset)
 