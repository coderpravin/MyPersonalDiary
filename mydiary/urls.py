from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add-entry', views.add_entry_view, name='add-entry'),
    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('logout/', views.login_view, name='logout'),
    path('delete-entry/<int:entry_id>', views.delete_entry_view, name='delete-entry'),
    
    
    
]
