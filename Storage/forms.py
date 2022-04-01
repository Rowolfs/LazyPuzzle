from django.core.exceptions import ValidationError
from django import forms
from .models import *

class AddVerbalRiddles_post(forms.ModelForm):
    class Meta:
        model = VerbalRiddles
        fields = ['question', 'answer', 'themes', 'basic_settings']

    def clean_question(self):
        question = self.cleaned_data['question']
        if len(question) > 150:
            raise ValidationError('Please minimaze question')
        return question

    def clean_answer(self):
        answer = self.cleaned_data['answer']
        if len(answer) > 20:
            raise ValidationError('Please minimaze answer')
        return answer
