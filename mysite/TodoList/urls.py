from django.urls import path
from .views import TaskViewSet

urlpatterns = [
    path('', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name = 'product_list'),
    path('<int:pk>/', TaskViewSet.as_view({'get': 'retrieve',
                                              'put': 'update', 'delete': 'destroy'}), name = 'product_detail')
]