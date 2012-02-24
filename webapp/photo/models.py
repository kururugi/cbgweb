from django.db import models
from imagekit.models import ImageSpec
from imagekit.processors import SmartResize

class Photo(models.Model):
    timestamp = models.DateField(auto_now=True)
    original_image = models.ImageField(upload_to='photos')
    thumbnail = ImageSpec([SmartResize(200, 200)], 
                    image_field='original_image',
                    format='JPEG',
                    options={'quality': 86})
