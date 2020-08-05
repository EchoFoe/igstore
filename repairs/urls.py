from django.urls import path
from . import views
app_name = 'repairs'

urlpatterns = [
    path('', views.repair_list, name='repair_list'),
    path('<slug:category_slug>/', views.repair_list, name='repairs_list_by_category'),
    path('<int:id>/<slug:slug>/', views.repair_detail, name='repair_detail'),
]
