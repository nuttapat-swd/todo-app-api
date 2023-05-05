from django.urls import path, include

from user import views

urlpatterns = [
    path('users',views.UserListView.as_view(),name='user-list'),
    
]
