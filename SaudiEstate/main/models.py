from django.db import models
from django.conf import settings  

class ContactMessage(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="messages")
    
    message = models.TextField(verbose_name="message")
    created_at = models.DateTimeField(auto_now_add=True)
    
    admin_reply = models.TextField(blank=True, null=True, verbose_name="admin reply")
    is_replied = models.BooleanField(default=False)
    replied_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Message from {self.user}"