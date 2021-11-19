from django.db import models

# Create your models here.
class csvmodel(models.Model):
    file_upload = models.FileField(upload_to="api")

    
    def __self__(self):
        return f"id : {self.id}"


class valueModel(models.Model):
    name = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=10,)

    def __self__(self):
        return f"name: {name}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)