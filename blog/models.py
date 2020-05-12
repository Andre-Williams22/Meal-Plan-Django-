from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title





# python manage.py makemigrations 
# python manage.py migrate 
# python manage.py shell 
# from blog.models import Post
# from django.contrib.auth.models import User 
# User.objects.all()
# User.objects.first()
# User.objects.filter(username='andre')
# User.objects.filter(username='andre').first 

# user = User.objects.filter(username='andre')
# or 
# user = User.objects.get(id=1)
# user

# post_1 = Post(title='Blog 1', content='First Post Content', author=user)
# post_1.save()

# post_2 = Post(title='Blog 2', content='Sky is beautiful', author_id=user.id)
# post_2.save()

# post = Post.objects.first()
# post.content 
# post.date_posted
# post.author.email
# user.post_set.all() ## shows all their post

