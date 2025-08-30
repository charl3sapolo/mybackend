from .views import *
from django.urls import path

urlpatterns = [
    path("items/", ItemList.as_view()),
    path("itemupdate/<int:pk>/", ItemUpdate.as_view()),
    path("companyreg/", CompanyEndpt.as_view()),
    path("receipt/", Receipt.as_view()),
]
