from django.urls import path
from . import views
from .views import (
    EmployeeCreateView,
    EmployeeListView,
    EmployeeDetailView,
    EmployeeUpdateView,
    SearchListView
)


urlpatterns = [
    path('employee/new/',
         EmployeeCreateView.as_view(), name='new-employee'),
    path('employee/all/',
         EmployeeListView.as_view(), name='all-employee'),

    path('employee/<int:pk>/update/',
         EmployeeUpdateView.as_view(), name='update-employee'),

    path('employee/<int:pk>/details/',
         EmployeeDetailView.as_view(), name='details-employee'),

    path('employee/<int:pk>/delete/',
         views.deleteEmployee, name='delete_employee'),

    path('search/', SearchListView.as_view(), name='search')

]
