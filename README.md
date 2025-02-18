# Meu Portfólio 2D

Este é um projeto de portfólio profissional desenvolvido com Django, utilizando PostgreSQL (recomendado versão 12 ou superior) e um sistema customizado de Math Captcha para evitar bots. O sistema permite:

- Cadastro e login de usuários com checagem de duplicidade de username/e-mail.
- Criação automática de um perfil de usuário.
- Envio de interesse (apenas uma vez por usuário, exceto para admin).
- Painel administrativo para que o superusuário visualize e responda aos interesses enviados – a resposta é enviada via e-mail (configurado com SMTP real ou console).
- Alternância entre tema claro e escuro (via toggle).
- Layout responsivo com Bootstrap e um estilo retrô inspirado em jogos 2D.

## Funcionalidades

- **Cadastro e Login:**  
  Registro com formulário protegido por um Math Captcha (ex.: “3 + 7 = ?”).  
  Verificação de duplicidade de usuário e e-mail.  
  Criação automática de um `UserProfile` para cada usuário.

- **Demonstração de Interesse:**  
  Usuários (não administradores) podem enviar uma única mensagem de interesse.  
  O administrador (superusuário) não pode enviar interesse.

- **Painel Administrativo:**  
  Acesso restrito a superusuários para visualizar todos os interesses não respondidos, com contagem de novas mensagens, e responder aos interessados via e-mail.

- **Tema Claro/Escuro:**  
  Botão de toggle para alternar entre temas.

- **Banco de Dados PostgreSQL:**  
  Configurado para uso com PostgreSQL (preferencialmente 12+), pronto para deploy em produção.

## Requisitos

- Python 3.8+
- Django 4.2.19
- PostgreSQL (versão 12 ou superior é recomendada)
- psycopg2-binary
- (Opcional) SMTP real para envio de e-mails (por exemplo, Gmail)

## Instalação e Configuração

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/seu-projeto.git
cd game_portfolio
```

### 2. Crie e Ative o Ambiente Virtual

No terminal, execute:

- **Windows:**
  ```bash
  python -m venv env
  env\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  python -m venv env
  source env/bin/activate
  ```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o PostgreSQL

Crie o banco de dados e o usuário (exemplo usando psql):

```sql
CREATE DATABASE portifolio;
CREATE USER postgres WITH ENCRYPTED PASSWORD '1234';
GRANT ALL PRIVILEGES ON DATABASE portifolio TO postgres;
```

### 5. Atualize as Configurações do Projeto

No arquivo `game_portfolio/settings.py`, ajuste as configurações do banco e do e-mail conforme seu ambiente:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portifolio',         # Nome do banco
        'USER': 'postgres',           # Usuário
        'PASSWORD': '1234',           # Senha
        'HOST': 'localhost',          # Host ou IP
        'PORT': '5432',               # Porta padrão
    }
}

# Configuração de e-mail real (exemplo com Gmail):
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu-email@gmail.com'
EMAIL_HOST_PASSWORD = 'sua-app-password'
```

Para testes, você pode usar o backend de console:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### 6. Execute as Migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crie um Superusuário (Opcional)

```bash
python manage.py createsuperuser
```

### 8. Rode o Servidor

```bash
python manage.py runserver
```

Acesse [http://127.0.0.1:8000](http://127.0.0.1:8000) no navegador.

## Estrutura do Projeto

```
game_portfolio/
├── manage.py
├── requirements.txt
├── game_portfolio/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── portfolio_app/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── templates/
    │   └── portfolio_app/
    │       ├── base.html
    │       ├── home.html
    │       ├── login.html
    │       ├── register.html
    │       ├── sobre.html
    │       ├── projetos.html
    │       ├── painel_interesses.html
    │       └── partials/
    │           ├── navbar.html
    │           └── footer.html
    └── static/
        ├── css/
        │   └── styles.css
        └── imgs/
            └── background.png
```

## Fluxo de Uso

- **Registro:**  
  Visite `/register` para se cadastrar. O formulário possui um Math Captcha (por exemplo, “3 + 7 = ?”) para evitar bots. O sistema checa duplicidade de username e e-mail e cria um UserProfile automaticamente.

- **Login:**  
  Visite `/login` para efetuar o login.

- **Sobre:**  
  A página `/sobre` exibe informações do seu perfil. Se você estiver logado e não for administrador, poderá enviar uma mensagem de interesse (apenas uma vez).

- **Projetos:**  
  Visite `/projetos` para ver seus projetos (atualmente exibido como "Em construção...").

- **Painel de Interesses:**  
  O superusuário pode acessar `/painel/interesses` para visualizar os interesses enviados, ver a contagem de novas mensagens (não respondidas) e responder aos interessados. Ao responder, um e-mail será enviado para o interessado (dependendo das configurações de e-mail).

## Notas de Produção

- **DEBUG:** Certifique-se de definir `DEBUG = False` no ambiente de produção e configurar `ALLOWED_HOSTS` corretamente.
- **SECRET_KEY:** Mantenha sua chave secreta protegida e não a exponha em repositórios públicos.
- **Deploy:** Para produção, considere usar Gunicorn e Nginx ou outro servidor WSGI.
- **Banco de Dados:** Atualize para uma versão recente do PostgreSQL (recomendado 12+) para compatibilidade com Django 4.2.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Basta abrir um pull request ou issue no repositório.

## Precisa: 
- Fazer o comentário de interesse ser notificado no e-mail da pessoa do painel
- Fazer o comentário da pessoa do painel ser notificado para a pessoa que demonstrou interesse
- icone de sol e lua no botão de tema
- bolinha com numeração na notificação do painel.
- Regra de que a pessoa só pode enviar 1 interesse até ser respondido, para evitar SPAM
- Ver alguma forma de verificar e-mail da pessoa registrada
- Alguma forma de evitar BOTS ( capcha ou verificação )
- colocar melhores projetos.
