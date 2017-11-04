from django.contrib.auth.models import User
from django import forms
# from .models import Registration


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password', 'email']

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email_ver')

        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email).first()
        if email_qs:
            raise forms.ValidationError("This email has already been registered")
        return email
