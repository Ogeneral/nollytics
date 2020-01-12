from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100, default='',null=True)
	age = models.PositiveIntegerField(blank=True,null=True)
	email = models.CharField(max_length=50, default='',null=True)
	phone = models.IntegerField(default=0,null=True)

	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
 	if kwargs['created']:
 		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class Post(models.Model):
    Your_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)   
    Your_Post_title = models.CharField(max_length=200)  
    Your_Post = models.TextField(max_length=2000)
    id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.Your_Post




