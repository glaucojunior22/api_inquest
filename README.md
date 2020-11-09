# Descrição da API:

- Registro de pessoas, a partir do CPF

- Registro de empresas e donos da empresa(podendo ser pessoas físicas e ou jurídicas, ou seja uma empresa que tem como dono uma outra empresa)

- Registro de bens e posses de um indivíduo

Requisitos da API:


- Desenvolvimento em Python 3+

- Boa cobertura de Testes unitários e outros testes que julgar necessários

- Documentação (pode ser docstrings ou um Markdown)

- Docker e/ou algum aparato de containerização e deployment

## Requisitos mínimos para executar o projeto:
É necessário ter o python e o pip instalados, depois basta rodar o comando:

`$ pip install docker-compose`

Para rodar a aplicação pela primeira vez rode as migrações do Django:

`$ docker-compose up migration`

Por último execute o docker-compose para executar o Django efetivamente:

`$ docker-compose up web`

Para acessar a documentação da API, com a aplicação rodando, abra o navegador em:

[Localhost](http://localhost:8000/api/v1)

Se tudo estiver certo, a seguinte página será exibida:

[Sucesso!](https://i.imgur.com/xwbkrVo.png)

Á partir daí podemos usar o próprio navegador para testar a API, por exemplo ao abrir o link: [Pessoas](http://localhost:8000/api/v1/person) podemos ver a listagem de pessoas e um formulário para criar novas pessoas. O funcionamento é o mesmo para [Empresas](http://localhost:8000/api/v1/enterprise) e [Posses](http://localhost:8000/api/v1/possession).

Caso queira executar os testes unitários execute o comando:

`$ docker-compose up unittests`

