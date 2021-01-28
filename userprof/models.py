from django.db import models

# Create your models here.


class userdb(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    age = models.IntegerField(default=1)
    skills = models.CharField(max_length=300)
    image1 = models.ImageField(upload_to="userprof/images", default="")
    image2 = models.ImageField(upload_to="userprof/images",default="")

    def __str__(self):
        return self.user_name