from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('profile/<int:pk>/', include([
        path('', views.show_profile_details, name='profile-details'),
        path('edit/', views.edit_profile, name='profile-edit'),
        path('delete/', views.delete_profile, name='profile-delete'),
    ])),

]
