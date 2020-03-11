from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

class ProfileTestCases(TestCase):
    def setUp(self):
        self.user = User(username='user', email='email')
        self.user.save()
        self.profile = Profile(image='image', bio='bio', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
    
    def tearDown(self) -> None:
        Profile.objects.all().delete()
    
    def test_save_user_profile(self):
        self.new_profile.save_user_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_user_profile(self):
        self.new_profile.save_user_profile()
        self.new_profile.delete_user_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_update_profile_bio(self):
        self.new_profile.save_user_profile()
        updated_profile = Profile.update_profile_bio(self.new_profile.id, 'bye')
        self.assertEqual(updated_profile.bio, 'bye')

    def test_update_profile_pic(self):
        self.new_profile.save_user_profile()
        updated_profile = Profile.update_profile_pic(self.new_profile.id, 'gp.jpg')
        self.assertTrue(updated_profile.profile_pic != self.new_profile.profile_pic)

class PostTestClass(TestCase):
    def setUp(self):
        self.post = Post(image='image',caption='caption',created_date='created_date')

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def tearDown(self) -> None:
        Image.objects.all().delete()
        User.objects.all().delete()
        Profile.objects.all().delete()
        
class CommentTestClass(TestCase):
    def setUp(self):
        self.comment = Comment(comment='comment', created_date='created_date')
        self.post = Post(image='image', caption='caption', created_date='created_date')
        self.post.save()
        self.user = User(username='user', email='email')
        self.user.save()


    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def test_save(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments)>0)
