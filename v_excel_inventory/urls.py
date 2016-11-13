"""v_excel_inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from people.views import CustomerViewset, InternalUserViewset
from production_system.views import TaskViewset, OrderViewset, ItemViewset, InventoryViewset, PurchaseViewset, \
    ProductionViewset, ProductInventoryViewset, RawMaterialViewset, TagViewset, InvoiceViewset
from service_and_process.views import MasterWorkableViewset, MasterProcessViewset, MasterProductViewset, MasterServiceViewset
from webapp.views import index, CustomerList, ServicesList

router = routers.DefaultRouter()

router.register(r'workable', MasterWorkableViewset)
router.register(r'customers', CustomerViewset)
router.register(r'users', InternalUserViewset)
router.register(r'tasks', TaskViewset)
router.register(r'services', MasterServiceViewset)
router.register(r'process', MasterProcessViewset)
router.register(r'products', MasterProductViewset)
router.register(r'orders', OrderViewset)
router.register(r'items', ItemViewset)
router.register(r'inventory', InventoryViewset)
router.register(r'purchase', PurchaseViewset)
router.register(r'production', ProductionViewset)
router.register(r'product_inventory', ProductInventoryViewset)
router.register(r'material', RawMaterialViewset)
router.register(r'tags', TagViewset)
router.register(r'invoice', InvoiceViewset)

api_urls = [
    url(r'^', include(router.urls))
]


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^customers_list', CustomerList.as_view()),
    url(r'^services_list', ServicesList.as_view())
]
