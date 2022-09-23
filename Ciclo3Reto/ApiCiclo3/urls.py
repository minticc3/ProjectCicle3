from django.urls import path
from .views import RolViews, EmployeeViews, ProfileView, EnterpriseViews, TransactionViews
from . import views

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

    #login
    path('login/',views.loginUser , name="Login"),

    #register
    path('newemployee/', views.formRegister, name="Formulario Nuevo Empleado"),
    
    #actualizar
    path('actualizaremp/<int:id>', views.formUpdate , name="Formulario Actualizar Empleado"),

    path('actualizae/', views.updateEmployee, name="Actualizar Empleado")
]