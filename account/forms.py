from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
	username = forms.CharField(max_length=150,widget=forms.TextInput(attrs={
		'class':'form__input','autocomplete':'username', 'id':'login__username',
		'placeholder':"Username"

		})
		)
	






class LoginForm1(forms.Form):

	
	password = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'type':"password",
		'class':'form__input','autocomplete':'password', 'id':'login__password',
		'placeholder':"password"})
		)






class Signup(forms.Form):

	
	password = forms.CharField(max_length=150,widget=forms.PasswordInput(attrs={'type':"password",
		'class':'form__input','autocomplete':'password', 'id':'signup__password',
		'placeholder':"password"})
		)
	




class Signup1(forms.Form):
	username = forms.CharField(max_length=150,widget=forms.TextInput(attrs={
		'class':'form__input','autocomplete':'username', 'id':'signup__username',
		'placeholder':"Username"

		})
		)
	# def clean_username(self):
	# 	if(User.objects.filter(username=self.cleaned_data['username']).exists()):
	# 		raise forms.ValidationError("username taken")
	# 	return self.cleaned_data['username']


class Signup2(forms.Form):
	firstname = forms.CharField(max_length=150,widget=forms.TextInput(attrs={
		'class':'form__input','autocomplete':'firstname', 'id':'first__name',
		'placeholder':"first name"

		})
		)	
	
class Signup3(forms.Form):
	lastname = forms.CharField(max_length=150,widget=forms.TextInput(attrs={
		'class':'form__input','autocomplete':'lastname', 'id':'last__name',
		'placeholder':"lastname"

		})
		)	