# models.py

from django.db import models
from django.urls import reverse
from django.utils import timezone


class BirdSpecies(models.Model):
    STATUS_CHOICES = [
        ('LC', 'Least Concern'),
        ('NT', 'Near Threatened'),
        ('VU', 'Vulnerable'),
        ('EN', 'Endangered'),
        ('CR', 'Critically Endangered'),
    ]
    My_choice =[
        ('LC', 'Least Concern'),
        ('NT', 'Near Threatened'),
        ('VU', 'Vulnerable'),
        ('EN', 'Endangered'),
        ('CR', 'Critically Endangered'),
    ]
    

    status_code = models.CharField(max_length=10, choices=STATUS_CHOICES)
    common_name = models.CharField(max_length=100, unique=True)
    scientific_name = models.CharField(max_length=100)
    bird_description = models.TextField(blank=True)
    current_status = models.CharField(max_length=10,choices= My_choice)
    wiki_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.common_name

class ClassifiedImage(models.Model):
    image = models.ImageField(upload_to='classified_images/')
    predicted_species = models.ForeignKey(BirdSpecies, on_delete=models.CASCADE, null=True)
    classified_at = models.DateTimeField(auto_now_add=True)
    confidence = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.predicted_species.common_name} - {self.classified_at}'

    def get_absolute_url(self):
        return reverse('classified-image-detail', args=[str(self.id)])
