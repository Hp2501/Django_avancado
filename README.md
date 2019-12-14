# Django-Avançado

Projeto Django-Avançado - curso Geek University


## Projeto apenas para fins **didáticos** não é um projeto **"real"** ##


Desenvolvido com Django 3.0 - Python 3.8 - PostgreSQL 12.1

-------------------------------------------------------------------------

## Como rodar o projeto? ##

```
git clone https://github.com/Hp2501/Django_avançado.git
cd Django_avançado
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Obs: configurar o *__python-decouple__* e *__dj_database_url__*


[como configurar](https://samuelgoncalves.com.br/configurar-sua-aplicacao-django-para-ler-dados-diferentes-por-ambiente/)


## Conhecimentos aplicados no Projeto ##


* Criação do projeto em PostegreSQL
* Modularização dos Templates
* Herança de Templates
* Class Based Views
* Context Manager
* Criação dos Forms
* Definindo templates
* Definindo models
* Forms e Class Based Views
* Deploy (Heroku)
