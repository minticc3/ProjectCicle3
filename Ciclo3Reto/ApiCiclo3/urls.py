from django.urls import path
from .views import RolViews

urlpatterns=[
    path('rol/',RolViews.as_view(), name="Get"),
    path('rol/<int:id>',RolViews.as_view(), name="Update"),
]