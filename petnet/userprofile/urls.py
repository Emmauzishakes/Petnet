from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "userprofile"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('my-store/', views.my_store, name="my_store"),
    path('my-store/add-product/', views.add_product, name="add_product"),
    path('my-store/edit-product/<int:pk>/', views.edit_product, name="edit_product"),
    path('my-store/delete-product/<int:pk>/', views.delete_product, name="delete_product"),
    path('vendor/<int:pk>/', views.vendor_detail, name="vendor_detail"),
]
