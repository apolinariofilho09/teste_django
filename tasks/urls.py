from django.urls import path
from tasks import views

app_name='tasks'
urlpatterns = [
    path('', views.Index.as_view(), name='Index'),
    path('task/<int:pk>/', views.Task.as_view(), name='Taskk'),
    path('create/', views.Create.as_view(), name='Create'),
    path('update/<int:pk>/', views.Update.as_view(), name='Update'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='Delete'),
    path('complete/<int:pk>/', views.Complete.as_view(), name='Complete'),
]