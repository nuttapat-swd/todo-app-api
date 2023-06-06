from django.urls import path, include

from user import views


app_name = 'user'
urlpatterns = [
    path('',views.UserListView.as_view(),name='user-list'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
]
