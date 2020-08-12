# Skoolit: Um sistema para um novo modelo de escola
Trabalho prático da disciplina de Engenharia de Software @ UFMG
Integrantes:
- Arthur Souto Lima
- Caio Guedes
- Gabriel Victor Carvalho
- Guilherme Bezerra
- Lucas Brant
- Luiz Felipe Mascarenhas Dalle Nery
---
## Especificações
### Descrição:
Skoolit será um sistema de gerenciamento escolar direcionado para alunos de idade de ensino fundamental e médio, onde haverão cadastros de aluno e professor. Nesse sistema, alunos serão livres para montar sua grade e escolher as matérias que quiserem se matricular em um dado semestre (com algumas limitações básicas). 

As aulas e materiais serão disponibilizadas online pelo professor que ministra a matéria, que também poderá elaborar e postar questionários. Adicionalmente, matérias similares poderão ser recomendadas aos alunos baseados nas matérias que já se matricularam.
### Tecnologia:
Será implementado um sistema web, usando HTML/CSS e JavaScript (com a framework Vue.js) para o front-end, Python (com a framework Flask) para o back-end e MySQL para gerenciamento de banco de dados em SQL.
### Fluxo de Desenvolvimento:
A branch master contém apenas versões com funcionalidades finalizadas e implementadas para avaliação do usuário. A branch develop contém as funcionalidades já desenvolvidas, mas ainda não empacotadas para o usuário final. 

O desenvolvimento de novas funcionalidades são feitos em branches paraleleas (feature), que assim que terminadas, são integradas com o develop. 

Os commits podem ser verificados em cada uma dessas branches.

---
## Sprint Planning
### Histórias
#### USUÁRIO
##### Login no sistema
> Como usuário, eu gostaria de entrar (fazer login) no sistema com e-mail e senha.
##### Visualizar informações
> Como usuário, eu gostaria de visualizar minhas principais informações, tais como turmas e disciplinas matriculadas, numa página inicial.
##### Visualizar postagens
> Como usuário, eu gostaria de ver as postagens nas turmas que estou inscrito.
##### Personalizar perfil
> Como usuário, eu gostaria de personalizar meu perfil com informações como nome, e-mail, senha e foto de perfil.

#### ADMINISTRADOR
##### Gerenciar usuários, matérias e turmas
> Como administrador, eu gostaria de cadastrar e gerenciar professores, alunos, disciplinas e turmas da escola.

#### ALUNO
##### Visualizar turmas disponíveis
> Como aluno, eu gostaria de ser capaz de ver as turmas disponíveis para inscrição e gostaria de ser capaz de me inscrever em uma turma disponível, caso cumpra os pré-requisitos e hajam vagas.

#### PROFESSOR
##### Criar postagem
> Como professor, eu gostaria de criar postagens nas turmas no qual eu sou professor. Em uma postagem, deve ser possível colocar uma mensagem de texto.
---

## Responsáveis
* Guilherme: Banco de dados e integração básica do sistema
* Lucas: Página e funcionalidade inicial
* Luiz: Página e funcionalidade de perfil e de alunos
* Arthur: Página e funcionalidade de login no sistema
* Gabriel: Página e funcionalidade de matérias/turmas
* Caio: Página e funcionalidade de professores
---

Link para o quadro scrum [aqui](https://www.notion.so/c8d063d8b5d14acc9a9753b623f2b15e?v=227ee1429a3b48ab828c705b3d6c29e4 "Quadro SCRUM")

## Arquitetura
![Diagrama de pacotes UML](https://drive.google.com/uc?export=view&id=1E-reJF9m6pdjns7_yjXq4wlQuw3BQtFv)

