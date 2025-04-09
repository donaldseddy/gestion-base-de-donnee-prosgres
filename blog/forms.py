from django import forms
from .models import BlogProduit
from django.contrib.gis.geos import Point

class BlogProduitForm(forms.ModelForm):
    latitude = forms.FloatField()
    longitude = forms.FloatField()

    class Meta:
        model = BlogProduit
        fields = ['name', 'ref', 'description', 'price', 'latitude', 'longitude']

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Création du point géographique
        latitude = self.cleaned_data['latitude']
        longitude = self.cleaned_data['longitude']
        instance.geolocalization = Point(longitude, latitude)
        instance.latitude = latitude
        instance.longitude = longitude

        if commit:
            instance.save()
        return instance
