from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from todoapp import views

router = DefaultRouter()

router.register('', views.TodoViewSet, basename='TodoViewSet')

urlpatterns = [
]
urlpatterns += router.urls
