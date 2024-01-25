from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from accounts import views

router = DefaultRouter()

router.register('', views.AccountViewSet, basename='accounts')

urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
]
urlpatterns += router.urls
