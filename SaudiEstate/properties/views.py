from django.contrib import messages
from django.shortcuts import render, get_object_or_404 , redirect
from .models import Property
from django.db.models import Q
from .models import Favorite
from django.contrib.auth.decorators import login_required


def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)

    is_favorited = False
    if request.user.is_authenticated:
        is_favorited = property.is_favorited_by(request.user)

    related_properties = Property.objects.filter(
        Q(city=property.city) | 
        Q(property_type=property.property_type) |
        Q(price__range=(float(property.price) * 0.8, float(property.price) * 1.2))
    ).exclude(pk=pk).distinct().order_by('?')[:3]

    context = {
        'property': property,
        'related_properties': related_properties,
        'is_favorited': is_favorited,
    }
    return render(request, 'properties/property.html', context)



@login_required
def toggle_favorite(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    
    favorite = Favorite.objects.filter(user=request.user, property=property_obj).first()

    if favorite:
        favorite.delete()
        messages.success(request, "Removed from favorites.")
    else:
        Favorite.objects.create(user=request.user, property=property_obj)
        messages.success(request, "Added to favorites.")

    return redirect('properties:detail', pk=pk)

@login_required
def remove_favorite(request, fav_id):
    favorite = get_object_or_404(Favorite, id=fav_id, user=request.user)
    favorite.delete()
    messages.success(request, "Property removed from favorites.")
    return redirect('users:profile')


def is_favorited_by(self, user):
    return self.favorite_set.filter(user=user).exists()


