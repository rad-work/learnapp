from django import forms
from .models import Post

CHOICES = [
    ('STU', 'Ученик'),
    ('TEA', 'Учитель'),
]


class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Логин',
            }
        )
    )
    first_name = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }
        )
    )
    last_name = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
            }
        )
    )
    email = forms.EmailField(
        max_length=20,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'e-mail',
            }
        )
    )
    password = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
            }
        )
    )
    status = forms.ChoiceField(
        choices=CHOICES)


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Логин',
            }
        )
    )
    password = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
            }
        )
    )


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Текущий пароль',
            }
        )
    )
    new_password = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Новый пароль',
            }
        )
    )


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'subject')

