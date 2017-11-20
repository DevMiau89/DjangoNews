from django.contrib.auth.models import User
from django import forms
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineField
from crispy_forms.helper import FormHelper
from .models import Article, Comment


class RegistrationForm(forms.ModelForm):
    email_ver = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password', 'email']

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.data.get('email_ver')
        print email
        print email2
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email).first()
        if email_qs:
            raise forms.ValidationError("This email has already been registered")
        return email


class LoadForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def __init__(self, *args, **kwargs):
        super(LoadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_action = '/'
        self.helper.layout = Layout(
            InlineField(
                'email'
            ),
            InlineField(
                'password'

            ),
            InlineField(
                Submit('sign in', 'Sign in', css_class='btn-submit')
            ),
        )


class AddArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddArticleForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_action = '#'
        self.helper.layout = Layout(
            'title',
            'text',
            'image',
            'author',
            'tags'
        )
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Article
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=35)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
