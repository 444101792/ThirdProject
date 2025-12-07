from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.utils import timezone
from .forms import ContactMessageForm, AdminReplyForm
from .models import ContactMessage
from properties.models import Property  

def home(request):    
    properties = Property.objects.filter(verification_status='approved').order_by('?')
    
    if request.user.is_authenticated:
        user_city = getattr(request.user, 'city', None)
        if user_city:
            city_properties = Property.objects.filter(verification_status='approved', city__icontains=user_city).order_by('-created_at')
            if city_properties.exists():
                properties = city_properties

    featured_properties = properties[:3]

    context = {
        'properties': featured_properties
    }
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, "main/about.html")

@login_required
def contact_us(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact_msg = form.save(commit=False)
            contact_msg.user = request.user
            contact_msg.save()
            
            return redirect('main:home') 
    else:
        form = ContactMessageForm()
    
    return render(request, 'main/contact_us.html', {'form': form})

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def admin_inbox(request):
    messages = ContactMessage.objects.select_related('user').all().order_by('-created_at')
    return render(request, 'main/admin_inbox.html', {'messages': messages})

@user_passes_test(is_superuser)
def reply_message(request, message_id):
    msg = get_object_or_404(ContactMessage, id=message_id)
    
    if request.method == 'POST':
        form = AdminReplyForm(request.POST, instance=msg)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.is_replied = True
            reply.replied_at = timezone.now()
            reply.save()

            try:
                html_content = render_to_string('main/email_reply.html', {
                    'name': msg.user.first_name or msg.user.username,
                    'original_message': msg.message,
                    'admin_reply': reply.admin_reply
                })
                text_content = strip_tags(html_content)

                email = EmailMultiAlternatives(
                    subject='Response from SaudiEstate Support',
                    body=text_content,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[msg.user.email]
                )
                email.attach_alternative(html_content, "text/html")
                email.send()
            except Exception as e:
                print(f"Error sending email: {e}")

            return redirect('main:admin_inbox')
    else:
        form = AdminReplyForm(instance=msg)

    return render(request, 'main/reply_message.html', {'form': form, 'msg': msg})