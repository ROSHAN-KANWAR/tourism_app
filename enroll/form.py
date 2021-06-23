from django import forms
from .models import District,Allpost,Gallerypost

##temple post
class Templeform(forms.ModelForm):
    class Meta:
        model = Allpost
        fields = ['name','district','file','type','dec']
##gallery post
class Galleryform(forms.ModelForm):
    class Meta:
        model = Gallerypost
        fields = ['name','district','file','type']

class Districtfilter(forms.ModelForm):
    class Meta:
        model=District
        fields=['district']


##temple photo add
class Templeaddphotos(forms.ModelForm):
    class Meta:
        model = Allpost
        fields = ['name','district','file','type','dec']

