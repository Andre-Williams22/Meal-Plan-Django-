from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Profile(models.Model):
    # create 1 to 1 relationship for each user and profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


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