from django.urls import path
from .views import RolViews

urlpatterns=[
    path('rol/',RolViews.as_view(), name="Get"),
    path('rol/<int:id>',RolViews.as_view(), name="Update"),

    path('Employee/',EmployeeViews.as_view(), name="Get"),
    path('Employee/<int:id>',EmployeeViews.as_view(), name="Update"),
    
]