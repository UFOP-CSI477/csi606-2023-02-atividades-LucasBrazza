
# Projeto de Doação de Sangue

Este projeto tem como objetivo criar um sistema para gerenciar doações de sangue. Ele utiliza o framework Django e o pacote Crispy-forms.

## Requisitos

- Python
- Pip (gerenciador de pacotes do Python)

## Instalação

1. Crie uma pasta para o projeto e navegue até ela no terminal.
2. Crie uma máquina virtual usando o comando: 
   ```python -m venv .venv```
3. Ative a máquina virtual usando o comando:
   - No Windows: 
```.venv\Scripts\activate```
   - No Linux: `source .venv/bin/activate`
1. Instale o Django e o Crispy-forms usando o comando: `pip install django crispy-forms`
2. Crie um novo projeto Django usando o comando: `django-admin startproject server`
3. Navegue até a pasta do projeto usando o comando: `cd server`
4. Crie um novo aplicativo Django chamado "donation" usando o comando: `python manage.py startapp donation`
5. Instale o Django Rest Framework usando o comando: `pip install djangorestframework`
6.  Adicione "rest_framework" e "donation" aos INSTALLED_APPS no arquivo settings.py do projeto.
7.  Crie um superusuário para o sistema usando o comando: `python manage.py createsuperuser`
8.  Inicie o servidor de desenvolvimento usando o comando: `python manage.py runserver`
9.  Acesse o endereço fornecido (geralmente http://127.0.0.1:8000/) para ver o sistema em execução.

## Testes

Para testar a API, acesse o painel de administração do Django (http://127.0.0.1:8000/admin/) e faça login com suas credenciais de superusuário.

Para testar o sistema completo, acesse o endereço fornecido (geralmente http://127.0.0.1:8