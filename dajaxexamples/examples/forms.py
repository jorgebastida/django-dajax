from django import forms

class ExampleForm(forms.Form):
	username = forms.CharField(max_length=30, label=u'Username')
	email = forms.EmailField(label=u'Email address')