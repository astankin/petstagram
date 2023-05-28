from django.urls import path, include

from petstagram.photos import views

urlpatterns = [
    path('add/', views.add_photo, name='add-photo'),
    path('<int:pk>/', views.photo_details, name='photo-details'),
    path('edit/<int:pk>/', views.photo_edit, name='photo-edit'),
    path('delete/<int:pk>/', views.delete_photo, name='photo-delete'),
]