from django import forms
#The "add to favorites" form
class AddFav(forms.Form):
	video = forms.CharField(required=False)