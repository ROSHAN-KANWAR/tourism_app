from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Contact,District,Typeofpost,Gallerypost,Allpost,Reviews


#contact your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','problem']


#District your models here.
@admin.register(District)
class Contact1Admin(ImportExportModelAdmin):
    list_display = ['id','district','urls','headquarter']

##type select only
@admin.register(Typeofpost)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id','type']


##Gallery post
@admin.register(Gallerypost)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id','name','file','district','type']



##All post
@admin.register(Allpost)
class AllpostAdmin(admin.ModelAdmin):
    list_display = ['id','name','file','district','type','dec']

##reviews
@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ['id','name','email','comment']