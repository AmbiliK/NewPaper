from django import forms
from users.models import SubscribedUser

class SubscribeForm(forms.ModelForm):
	class Meta:
		model = SubscribedUser
		fields = ['name', 'email']