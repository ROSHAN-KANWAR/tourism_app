import django_filters
from .models import Allpost,Gallerypost
class Filterpost(django_filters.FilterSet):
    class Meta:
        model=Allpost
        fields=['district']

class Filtergallery(django_filters.FilterSet):
    class Meta:
        model=Gallerypost
        fields=['district']