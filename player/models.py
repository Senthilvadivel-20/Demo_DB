from distutils.command.upload import upload
from email.policy import default
from django.db import models

# IPL player DataBase
class player(models.Model):
    Name = models.CharField(max_length=40,null=False,default="No Data")
    Team = models.CharField(max_length=10,null=False)
    No = models.IntegerField()
    Image = models.ImageField(upload_to='player_image/',blank=True)

    def __str__(self):
        return self.Name
