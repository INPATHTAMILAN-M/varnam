from django.urls import path
from events.viewsets.event import EventViewSet
from events.viewsets.department import DepartmentViewSet
from events.viewsets.ticket_pass import PassViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'passes', PassViewSet, basename='pass')

urlpatterns = router.urls