# Sistema de Controle Financeiro - PIT (Projeto Integrado Transdisciplinar)

## 1. Sobre o Projeto
O **Sistema de Controle Financeiro** é uma aplicação web desenvolvida como parte do Projeto Integrado Transdisciplinar (PIT). O objetivo principal da solução é oferecer uma ferramenta intuitiva, ágil e confiável para o gerenciamento de finanças pessoais, permitindo o registro de receitas e despesas, a categorização de movimentações, o cálculo automático de saldo e a limpeza segura do histórico de lançamentos.

## 2. Arquitetura e Tecnologias Utilizadas
O sistema foi projetado seguindo as boas práticas de engenharia de software, adotando o padrão arquitetural **MVC (Model-View-Controller)** para garantir a separação de responsabilidades, facilidade de manutenção e escalabilidade:

* **Backend (Controller):** Desenvolvido em **Python** utilizando o microframework **Flask**, responsável pelo gerenciamento de rotas, processamento de requisições e integração entre a interface e o banco de dados.
* **Persistência de Dados (Model & SGBD):** Utilizou-se o **SQLite**, um Sistema Gerenciador de Banco de Dados (SGBD) relacional amplamente consolidado no mercado. A escolha justifica-se pela sua alta confiabilidade, conformidade com o padrão SQL, baixa necessidade de manutenção e por dispensar servidores externos complexos, otimizando tanto o ambiente de desenvolvimento quanto a implantação em nuvem.
* **Frontend (View):** Construído com **HTML5** e **CSS3** modularizado (`static/css/style.css`), priorizando usabilidade, clareza visual e responsividade.
* **Hospedagem / Deploy:** Aplicação configurada e validada em ambiente de produção na plataforma **Render**.

## 3. Estrutura de Diretórios
A organização do repositório reflete a divisão modular do projeto:

```text
controle-financeiro/
├── static/
│   └── css/
│       └── style.css          # Estilização modular da interface
├── templates/
│   └── index.html             # Interface principal da aplicação (View)
├── tests/
│   └── tests_finance.py       # Suíte de testes automatizados (unittest)
├── app.py                     # Rotas e regras de controle (Controller)
├── models.py                  # Conexão e operações com o banco SQLite (Model)
├── financas.db                # Arquivo do banco de dados SQLite
├── requirements.txt           # Dependências do projeto Python
└── README.md                  # Documentação técnica do projeto
