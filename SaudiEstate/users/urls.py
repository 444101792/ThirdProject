from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),     
    path('logout/', views.logout_user, name='logout'),
    path("profile/", views.user_profile, name="profile"),
    path("edit/", views.edit_profile, name="edit_profile"),

path('reset_password/', 
         auth_views.PasswordResetView.as_view(
             template_name="users/password_reset.html",
             email_template_name="users/password_reset_email.html",
             success_url=reverse_lazy('users:password_reset_done') 
         ), 
         name='password_reset'),

    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_sent.html"), 
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name="users/password_reset_form.html",
             success_url=reverse_lazy('users:password_reset_complete')
         ), 
         name='password_reset_confirm'),

    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_done_complete.html"), 
         name='password_reset_complete'),


]