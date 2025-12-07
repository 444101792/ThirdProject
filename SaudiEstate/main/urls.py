from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_us, name='contact_us'),
    path('dashboard/messages/', views.admin_inbox, name='admin_inbox'),
    path('dashboard/reply/<int:message_id>/', views.reply_message, name='reply_message'),
    


]