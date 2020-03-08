from django.test import TestCase

# Create your tests here.
class ProfileTestClass(TestCase):
    def setup(self):
        self.user = User(username='user', email='email')
        self.user.save()
        self.profile = Profile(image='image', bio='bio', user=self.user)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)
