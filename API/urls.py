from rest_framework.routers import DefaultRouter
from API.views import EmployeeViewSet, OrganizationViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'employees', EmployeeViewSet)
ROUTER.register(r'organizations', OrganizationViewSet)

urlpatterns = ROUTER.urls
