# Eventex

Sistema de Eventos encomendados pela Morena

[![Build Status](https://travis-ci.org/mark-kns/eventex-wttd.svg?branch=master)](https://travis-ci.org/mark-kns/eventex-wttd)
[![Code Climate](https://codeclimate.com/github/mark-kns/eventex-wttd/badges/gpa.svg)](https://codeclimate.com/github/mark-kns/eventex-wttd)
[![Code Health](https://landscape.io/github/mark-kns/eventex-wttd/master/landscape.svg?style=flat)](https://landscape.io/github/mark-kns/eventex-wttd/master)
## Como desenvolver?

1. Clone o repositório.
2. Crie o virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env. 
6. Execute os teste.

```console
git clone https://github.com/mark-kns/eventex-wttd.git eventex-wttd
cd eventex-wttd
python -m venv .wttd
source .wttd/bin/activate
pip -r install requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```



## Como fazer o deploy?

1. Crie uma instância no Heroku.
2. Envie as configurações para o Heroku.
3. Define uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False.
5. Configure o serviço de email.
6. Envie o código para o Heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
git push heroku master --force
```
