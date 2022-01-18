# Processo Seletivo

RESTful API proposta no processo seletivo da Frexco.

## Dependências
- django 4.0.1
- djangorestframework 3.13.1
- django-cors-headers 3.11.0

## Instruções

Foi criada uma aplicação com duas API's, uma para a tabela das Frutas e outra para as Regiões. Sendo que dentro da tabela das frutas existe uma ForeignKey ligando à tabela das regiões.

Como virtual environment, foi utilizado o pipenv, que deve ser iniciado pelo comando: 

	pipenv shell

Para instalar as dependências:

	pipenv install django djangorestframework django-cors-headers

Para iniciar a API, dentro da pasta que contém o arquivo manage.py, pelo terminal, deve-se rodar o comando:

	python manage.py runserver

Para utilizar a API, é necessário acessar através de um navegador (ou alguma ferramenta para testar API's como o Postman) as URLs:

- <https://localhost:8000/api/fruit/>
- <https://localhost:8000/api/region/>

Ao final do caminho, é possível adicionar /id para acessar um item específico:

- <https://localhost:8000/api/fruit/1/> -> acessa o primeiro item da tabela Fruit

Ao acessar um item especifico de uma API, é possível utilizar os quatro verbos HTTP propostos (GET, PUT, PATCH, DELETE).

Por padrão é utilizada a porta 8000, porém poderá variar.

