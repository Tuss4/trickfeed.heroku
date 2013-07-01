from django import forms

class New_user(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField()