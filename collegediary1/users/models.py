from django.db import models
from django.contrib.auth.models import User
# from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    # image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    bio = models.CharField(max_length=300, default = "Hey there! I'm on django blog")
    tag = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # img = Image.open(self.image.path)
        #
        # if img.height > 200 or img.width > 200:
        #     output_size = (100,100)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)


    #def get_absolute_url(self):
    #    return reverse('profile',kwargs = {'pk': self.user.pk})
