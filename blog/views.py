from django.shortcuts import render
from .models import BlogProduit
from django.contrib.gis.geos import Point
from django.contrib.gis.db import models
from django.http import HttpResponse


"""une fonction qui permet d'enregistrer un produit dans la base de données"""
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # Create a Point object for the location
        location = Point(float(longitude), float(latitude))

        # Create and save the product instance
        product = BlogProduit(
            name=name,
            description=description,
            price=price,
            latitude=latitude,
            longitude=longitude,
            geolocalization=location
        )
        product.save()

    return render(request, 'add_product.html')


from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import BlogProduit
from .forms import BlogProduitForm

class BlogProduitCreateView(CreateView):
    model = BlogProduit
    form_class = BlogProduitForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('product_add')  # redirection après succès

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Produit ajouté avec succès ✅")
        return response
