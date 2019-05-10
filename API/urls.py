from rest_framework.routers import DefaultRouter
from API.views import EmployeeViewSet, OrganizationViewSet, AttachmentViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'employees', EmployeeViewSet)
ROUTER.register(r'organizations', OrganizationViewSet)
ROUTER.register(r'attachments', AttachmentViewSet)

urlpatterns = ROUTER.urls
