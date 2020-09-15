from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    # image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    bio = models.CharField(max_length=300, default = "Hey there! I'm on django blog")
    tag = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    #def get_absolute_url(self):
    #    return reverse('project-detail',kwargs = {'pk': self.user.pk})
