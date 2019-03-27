from django.urls import path
from . import views
from .views import HomePageView, DepartmentCreateView


urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('department/new/', DepartmentCreateView.as_view(),
         name='new-department'),
    path('department/<int:id>/delete/',
         views.deleteDepartment, name='delete_department'),
]
