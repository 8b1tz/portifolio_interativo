from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    link_demo = models.URLField(blank=True, null=True)
    link_github = models.URLField(blank=True, null=True)
    imagem = models.ImageField(upload_to='projetos_imagens/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Interesse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    mensagem = models.TextField(blank=True, null=True)
    respondido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.data.date()}"
