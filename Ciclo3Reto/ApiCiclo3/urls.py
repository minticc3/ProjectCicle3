from django.urls import path
from .views import RolViews, EmployeeViews, ProfileView, EnterpriseViews, TransactionViews

urlpatterns=[
    path('rol/',RolViews.as_view(), name="Get-Insert"),
    path('rol/<int:id>',RolViews.as_view(), name="Update-Delete"),

    path('profile/',ProfileView.as_view(), name="Get-Insert"),
    path('profile/<int:id>',ProfileView.as_view(), name="Update-Delete"),

    path('enterprise/',EnterpriseViews.as_view(), name="Get-Insert"),
    path('enterprise/<int:id>',EnterpriseViews.as_view(), name="Update-Delete"),

    path('employee/',EmployeeViews.as_view(), name="Get-Insert"),
    path('employee/<int:id>',EmployeeViews.as_view(), name="Update-Delete"),

    path('transaction/',TransactionViews.as_view(), name="Get-Insert"),
    path('transaction/<int:id>',TransactionViews.as_view(), name="Update-Delete"),
    
]