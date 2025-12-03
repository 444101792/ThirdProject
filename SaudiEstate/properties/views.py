from django.shortcuts import render, get_object_or_404
from .models import Property
from django.db.models import Q

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    related_properties = Property.objects.filter(
        Q(city=property.city) | 
        Q(property_type=property.property_type) |
        Q(price__range=(float(property.price) * 0.8, float(property.price) * 1.2))
    ).exclude(pk=pk).distinct().order_by('?')[:3] 

    context = {
        'property': property,
        'related_properties': related_properties
    }
    return render(request, 'properties/property.html', context)