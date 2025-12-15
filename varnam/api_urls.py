from django.urls import path, include
from rest_framework.routers import DefaultRouter
from varnam.viewsets.department import DepartmentViewSet
from varnam.viewsets.event import EventViewSet
from varnam.viewsets.pass import PassViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'events', EventViewSet, basename='event')
router.register(r'passes', PassViewSet, basename='pass')

urlpatterns = [
    path('', include(router.urls)),
]
