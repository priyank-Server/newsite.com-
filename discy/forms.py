from django import forms
from discy.models import *


class UserForm(forms.ModelForm):
    confirm_password = forms.PasswordInput()

    class Meta:
        model = MyUser
        fields = '__all__'

    # def is_valid(self):
    #     if MyUser.objects.filter(email=self.data['email']).exists():
    #         raise forms.ValidationError({"error": "user is already exist"})
    #     return self.data


class Askquestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'question_category', 'user', 'first_name', 'last_name']


class Postanswer(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'question_id', 'user']
