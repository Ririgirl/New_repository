from django import forms
from .models import *

class CandForm(forms.ModelForm):
		class Meta:
			model = Cand
			exclude = ['his_jedi']
			fields = ['name','age','planet','email','num_answer']

class QuestionForm(forms.ModelForm):
		class Meta:
				model = Answer
				fields = ['answer']
