from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Post(models.Model):
    image = CloudinaryField('images', null=True)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE, null=True)
    caption = models.CharField(max_length=200)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, blank=True, null=True)
    likes = models.ManyToManyField(User,related_name='likes', blank=True)
    posted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} Post'

    def save_image(self):
        return self.save()
  
    def delete_image(self):
        return self.delete()

    def add_likes(self):
        self.save()
        
    def update_image(self):
        return self.update()
        
    @classmethod
    def update_caption(cls, id, caption):
        cls.objects.filter(id=id).update(image_caption=caption)
        updated_caption = cls.objects.get(id=id)
        return updated_caption   

    @classmethod
    def get_post(cls,id):
        try:
            post = Post.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise Http404()
        return post

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    bio = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        db_table = 'profile'

    def save_user_profile(self):
        self.save()
        
    def delete_user_profile(self):
        self.delete()

    @classmethod
    def update_profile_pic(cls, id,image):
        cls.objects.filter(id=id).update(image=image)
        updated_profile_pic = cls.objects.get(id=id)
        return updated_profile_pic
    # Create Profile when creating a User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Save Profile when saving a User
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.post.author}, {self.user.username}'

    def save_comment(self):
        self.save()

    class Meta:
        db_table = 'comment'

