from django.db import models
import datetime as dt
import django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    image = CloudinaryField('images')
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    caption = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    posted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} Image'

    def save_image(self):
        return self.save()
  
    def delete_image(self):
        return self.delete()

    def update_image(self):
        return self.update()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics/')
    bio = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username} Profile'

    


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.post.author}, {self.user.username}'

    def save_comment(self):
        self.save()

class Following(models.Model):
    users = models.ManyToManyField(User, related_name='friend_set')
    current_user = models.ForeignKey(User, related_name='owner', on_delete=models.PROTECT, null=True)
