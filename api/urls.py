from rest_framework.routers import DefaultRouter
from api.views import EmployeeViewSet, OrganizationViewSet, AttachmentViewSet, EmployeeTableViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'employees', EmployeeViewSet)
ROUTER.register(r'employees-table', EmployeeTableViewSet)
ROUTER.register(r'organizations', OrganizationViewSet)
ROUTER.register(r'attachments', AttachmentViewSet)

urlpatterns = ROUTER.urls
