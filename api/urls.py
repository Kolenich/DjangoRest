from rest_framework.routers import DefaultRouter
from api.views import EmployeeViewSet, EmployeeTableViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'employees', EmployeeViewSet)
ROUTER.register(r'employees-table', EmployeeTableViewSet)

urlpatterns = ROUTER.urls
