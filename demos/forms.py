from django import forms
from django.core.exceptions import ValidationError


class SimpleForm(forms.Form):
    first_number = forms.CharField(max_length=10)
    second_number = forms.CharField(max_length=20)

    def process(self):
        a = self.cleaned_data["first_number"]
        b = self.cleaned_data["second_number"]
        return int(a) + int(b)

    def clean(self):
        cleaned_data = super().clean()
        a = cleaned_data.get("first_number")
        b = cleaned_data.get("second_number")
        if int(a) + int(b) > 10:
            raise ValidationError("Adding to more than 10 is impossible!")
