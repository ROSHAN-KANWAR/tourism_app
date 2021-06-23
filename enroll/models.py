from django.db import models

#contact details
class Contact(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    problem=models.TextField(max_length=1500)

##District tables
class District(models.Model):
    district=models.CharField(max_length=60)
    urls=models.URLField()
    headquarter=models.CharField(max_length=56)

    def __str__(self):
        return self.district
#Type select only
class Typeofpost(models.Model):
    type=models.CharField(max_length=100)

    def __str__(self):
        return self.type


#Gallery post
class Gallerypost(models.Model):
    name=models.CharField(max_length=100)
    file = models.FileField('Image_view', upload_to="gallery", default="")
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    type=models.ForeignKey(Typeofpost,on_delete=models.CASCADE)


##All post
class Allpost(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField('Image_view', upload_to="allpost", default="")
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    type = models.ForeignKey(Typeofpost, on_delete=models.CASCADE)
    dec=models.TextField(max_length=2000)


##reviews
class Reviews(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    comment=models.TextField(max_length=1500)