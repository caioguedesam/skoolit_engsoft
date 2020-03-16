# Skoolit: Um sistema para um novo modelo de escola
Trabalho prático da disciplina de Engenharia de Software @ UFMG
Integrantes:
- Arthur Souto Lima
- Caio Guedes
- Gabriel Victor Carvalho
- Guilherme Bezerra
- Lucas Brant
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
### Estórias
##### 1. Banco de Dados (1 Tulio)

- Modelagem UML
- Criação das tabelas

##### 2. Login (2 Tulios)

- Página de login
- Sistema de login

##### 3. Página Inicial (3 Tulios)

- Tarefas pendentes
- Matérias matriculadas
- Botões para outras páginas
- Deslogar

##### 4. Página de Perfil (4 Tulios)
 
- Matricular em matérias
- Visualização de dados do usuário
- Alteração de dados do usuário

##### 5. Página de Matérias (8 Tulios)

- Informações da matéria
- Atividades e materiais
- Aulas

Link para o quadro scrum [aqui](https://www.notion.so/c8d063d8b5d14acc9a9753b623f2b15e?v=227ee1429a3b48ab828c705b3d6c29e4 "Quadro SCRUM")

## Arquitetura
![Diagrama de pacotes UML](https://drive.google.com/uc?export=view&id=1E-reJF9m6pdjns7_yjXq4wlQuw3BQtFv)

