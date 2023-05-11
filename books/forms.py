from .models import Book 
from django import forms

from django.contrib.gis.geos import Point
from location_tools.object import nom


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'description', 'cover_image', 'location']
        exclude = ['author', 'slug', 'uuid', 'timestamp', 'owner']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Book Title'}),
            # current value of the field is set to 'Select Book Category' by default
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Book Category'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Book Description'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Upload Book Cover Image'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Book Location'}),
        }

    def clean_location(self):
        location = self.cleaned_data['location']
        point = nom.geocode(location)
        if point:
            return Point(point.longitude, point.latitude)
        else:
            raise forms.ValidationError('Please enter a valid location.')
        

    

    

#  views.py

