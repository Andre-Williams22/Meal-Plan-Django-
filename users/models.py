from django.db import models
from django.contrib.auth.models import User 
from PIL import Image
# Create your models here.

class Profile(models.Model):
    # create 1 to 1 relationship for each user and profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f" {self.user.username} Profile"





# python manage.py makemigrations 
# python manage.py migrate 

# python manage.py shell 
# user = User.objects.filter(username='andre').first() 
# user
# user.profile
# user.profile.image
# user.profile.url