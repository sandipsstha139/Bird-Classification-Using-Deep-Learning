from django.contrib import admin
from django.utils.html import format_html
from .models import BirdSpecies, ClassifiedImage

class BirdSpeciesAdmin(admin.ModelAdmin):
    list_display = ['status_code', 'current_status', 'common_name', 'scientific_name', 'bird_description']
    search_fields = ['common_name', 'scientific_name']
    list_per_page = 20

admin.site.register(BirdSpecies, BirdSpeciesAdmin)


class ClassifiedImageAdmin(admin.ModelAdmin):
    list_display = ['image_preview', 'predicted_species_name', 'classified_at_formatted']
    search_fields = ['predicted_species__name']
    list_filter = ['predicted_species', 'classified_at']
    date_hierarchy = 'classified_at'
    list_per_page = 20

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.image.url)

    def predicted_species_name(self, obj):
        return obj.predicted_species.common_name if obj.predicted_species else '-'

    def classified_at_formatted(self, obj):
        return obj.classified_at.strftime("%Y-%m-%d %H:%M:%S")

    image_preview.short_description = 'Image Preview'
    predicted_species_name.short_description = 'Pr edicted Species'
    classified_at_formatted.short_description = 'Classified At'

    fieldsets = (
        ('Image Information', {
            'fields': ('image_preview', 'predicted_species_name', 'classified_at_formatted'),
        }),
    )

    readonly_fields = ('image_preview', 'predicted_species_name', 'classified_at_formatted')

admin.site.register(ClassifiedImage, ClassifiedImageAdmin)
