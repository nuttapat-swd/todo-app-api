from django.urls import path, include

from user import views


app_name = 'user'
urlpatterns = [
    path('users',views.UserListView.as_view(),name='user-list'),

]
