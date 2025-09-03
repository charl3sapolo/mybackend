from .views import *
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("items/", ItemList.as_view()),
    path("itemupdate/<int:pk>/", ItemUpdate.as_view()),
    path("companyreg/", CompanyEndpt.as_view()),
    path("receipt/", Receipt.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
