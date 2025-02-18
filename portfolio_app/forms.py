import random

from django import forms


class MathCaptchaField(forms.IntegerField):
    def __init__(self, *args, **kwargs):
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.question = f"{self.num1} + {self.num2} = ?"
        self.answer = self.num1 + self.num2
        label = kwargs.pop('label', f"Resolva: {self.question}")
        super().__init__(label=label, *args, **kwargs)

    def validate(self, value):
        super().validate(value)
        if value != self.answer:
            raise forms.ValidationError("Resposta incorreta. Tente novamente.")

class RegisterForm(forms.Form):
    username = forms.CharField(label='Usuário')
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)
    captcha = MathCaptchaField()
