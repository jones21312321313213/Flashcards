from django.urls import path
from . import views

urlpatterns = [
    # Main notification list view
    path('', views.NotificationListView.as_view(), name='notification_list'),
    path('<int:pk>/read/', views.NotificationMarkAsReadView.as_view(), name='notification_read'),

]