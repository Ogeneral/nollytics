from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class SignUpForm(UserCreationForm):
	username = forms.CharField(max_length=254, help_text='')

	class Meta:
		model = User
		fields = (
				'username',
				'first_name',
				'last_name',
				'email',
		 )
		 
	def save(self, commit=True):
		user = super(SignUpForm, self).save(commit=False)
		user.first_name = user.first_name
		user.last_name = user.last_name
		user.email = user.email
	
		if commit:
				 user.save()
				
		return user
			
				 
class EditProfileForm(UserChangeForm):
	class meta:
		model = User
		fields = (
				'email',
				'password',
				'first_name',
				'last_name',
				
		 )	




class ImageUploadForm(forms.Form):
    image = forms.ImageField()
		 


		 
