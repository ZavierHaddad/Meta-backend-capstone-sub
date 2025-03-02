from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.api_root, name='api-root'),
    path('menu/', views.MenuItemView.as_view(), name = 'menu-list'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name = 'menu-detail'),
    path('user/', views.UserListView.as_view(), name = 'user-list'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name = 'user-detail'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'), #send post request here with username and password to get token
]