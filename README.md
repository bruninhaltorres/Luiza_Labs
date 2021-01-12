# Luiza_Labs
Passo a passo:

Iniciei criando o repositorio aqui no github e clonando na minha maquina. 
Ativei a vienv: Windows: Entrei na pasta Scripts e executei ". activate").
Criei o projeto: django-admin startproject <nome_do_projeto>
Entrei na pasta criada e criei o app: python manage.py startapp <nome_do_app>
Executei os comandos: 
python manage.py makemigrations 
python manage.py migrate
winpty python manage.py createsuperuser
python manage.py runserver
Entrei no servidor e busquei : localhost:8000/admin

Fiz o git add .
git commit -m "<mensagem>"
git push
