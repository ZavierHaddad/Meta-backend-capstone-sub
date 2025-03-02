"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet

router = DefaultRouter()
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')), #api-root is registerd here 1st so overides default routers root api
    path('restaurant/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

# Djoser provides a set of REST endpoints to handle user authentication.
# Here are some useful endpoints and their descriptions:

# Endpoint to register a new user
# POST /auth/users/
# Example: {"username": "newuser", "password": "newpassword"}

# Endpoint to get the current authenticated user's details
# GET /auth/users/me/

# Endpoint to activate a user account (usually used with email activation)
# POST /auth/users/activation/
# Example: {"uid": "user_id", "token": "activation_token"}

# Endpoint to resend activation email
# POST /auth/users/resend_activation/
# Example: {"email": "user@example.com"}

# Endpoint to set a new password for the current authenticated user
# POST /auth/users/set_password/
# Example: {"current_password": "oldpassword", "new_password": "newpassword"}

# Endpoint to reset password (usually used with email reset)
# POST /auth/users/reset_password/
# Example: {"email": "user@example.com"}

# Endpoint to confirm password reset
# POST /auth/users/reset_password_confirm/
# Example: {"uid": "user_id", "token": "reset_token", "new_password": "newpassword"}

# Endpoint to login and obtain an authentication token
# POST /auth/token/login/
# Example: {"username": "user", "password": "password"}

# Endpoint to logout and delete the authentication token
# POST /auth/token/logout/