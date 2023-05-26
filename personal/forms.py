from django import forms
from .models import PersonalInfo, Progress


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['user', 'name', 'surname', 'mobile', 'instagram', 'mass', 'height', 'email', 'sex', 'birthdate', 'level']

    def __init__(self, *args, **kwargs):
        super(PersonalInfoForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['surname'].required = False
        self.fields['mobile'].required = False
        self.fields['instagram'].required = False
        self.fields['mass'].required = False
        self.fields['height'].required = False
        self.fields['email'].required = False
        self.fields['sex'].required = False
        self.fields['birthdate'].required = False
        self.fields['level'].required = False


class PersonalProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['mass', 'hips', 'arms', 'chest', 'legs', 'waist', 'user']

    def __init__(self, *args, **kwargs):
        super(PersonalProgressForm, self).__init__(*args, **kwargs)
        self.fields['mass'].required = False
        self.fields['hips'].required = False
        self.fields['arms'].required = False
        self.fields['chest'].required = False
        self.fields['legs'].required = False
        self.fields['waist'].required = False
