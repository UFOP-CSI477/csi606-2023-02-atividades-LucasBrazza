# **CSI606-2021-02 - Remoto - Trabalho Final - Resultados**

## *Aluna: Princesa Leia (Luke Skywalker)*

--------------

### Resumo

Este trabalho apresenta o desenvolvimento de um sistema de reserva de assentos em viagens, visando facilitar a busca e reserva de viagens entre diferentes cidades. Destaco que as funcionalidades de login e autenticação de usuários não foram implementadas, e alguns CRUDs básicos não foram incluídos devido a decisões de escopo.

### 1. Funcionalidades implementadas

- Desenvolvi um sistema de busca de viagens por cidade de origem e destino.
- Implementei a exibição de viagens disponíveis para o dia selecionado.
- Criei a possibilidade de reserva de assentos em viagens selecionadas.
- Adicionei funcionalidades para que motoristas possam registrar veículos, indicar quantidade de lugares disponíveis e disponibilizar viagens.

### 2. Funcionalidades previstas e não implementadas

- Planejei a implementação de um sistema de autenticação para usuários e motoristas.
  - Justificativa: Optei por não implementá-lo devido a restrições de tempo e complexidade técnica. Meu foco estava direcionado para as funcionalidades principais do sistema.
- Decidi não incluir alguns CRUDs básicos, como visualização de todos os usuários ou edição de veículos.
  - Justificativa: Priorizei funcionalidades diretamente relacionadas à reserva de assentos em viagens, deixando funcionalidades administrativas de lado.

### 3. Outras funcionalidades implementadas

(Não se aplica)

### 4. Principais desafios e dificuldades

- **Problemas com o método update**: Enfrentei dificuldades na implementação do método update para reservas de assentos, pois estava causando inconsistências nos dados do sistema. Esses problemas foram resolvidos por meio de revisões no código e testes mais rigorosos.
- **Problemas com o método login**: Identifiquei dificuldades na implementação do método de login, principalmente na integração com o sistema de autenticação. Foram necessárias várias iterações e consultas à documentação para resolver esses problemas.

### 5. Instruções para instalação e execução

Para criar um ambiente virtual e instalar as dependências necessárias, siga os passos abaixo:

1. Abra o terminal e navegue até o diretório onde deseja criar o ambiente virtual.
2. Execute o comando `python -m venv myenv` para criar o ambiente virtual. Substitua "myenv" pelo nome que desejar.
3. Ative o ambiente virtual com o comando `source myenv/bin/activate` (Linux/Mac) ou `myenv\Scripts\activate` (Windows).
4. Com o ambiente virtual ativado, instale as dependências usando o pip:
`pip install django djangorestframework django-bootstrap-v5`


### 6. Referências

(Referências podem ser incluídas, caso necessário, seguindo o padrão ABNT.)

Youtube. Criando um ambiente virtual com Python (venv) - Curso de Python #10. Disponível em: https://www.youtube.com/watch?v=A_j5TAhY3sw. Acesso em: [coloque a data de acesso aqui, por exemplo: 18 fev. 2024].

Django REST Framework. Disponível em: https://www.django-rest-framework.org. Acesso em: [coloque a data de acesso aqui].

Django Documentation. Models - Django documentation. Disponível em: https://docs.djangoproject.com/en/5.0/topics/db/models/. Acesso em: [coloque a data de acesso aqui].

Youtube. Django Tutorial for Beginners - Full Course. Disponível em: https://www.youtube.com/watch?v=ElYj7lI3YMQ. Acesso em: [coloque a data de acesso aqui].

