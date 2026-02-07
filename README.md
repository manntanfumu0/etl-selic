```markdown
# 📊 ETL SELIC – Engenharia de Dados

Este projeto implementa um **pipeline de dados (ETL)** para coletar, transformar e organizar dados da **taxa SELIC**, seguindo boas práticas de Engenharia de Dados.

O objetivo é demonstrar, na prática, como estruturar um projeto de dados real, desde a extração até a transformação, com organização de pastas, versionamento e código limpo.

---

## 🚀 Objetivo do Projeto

- Extrair dados da taxa SELIC a partir de uma fonte pública  
- Transformar os dados para um formato limpo e estruturado  
- Organizar os dados seguindo o padrão **raw → processed**  
- Criar uma base sólida para consumo analítico futuro  
- Servir como projeto de portfólio para **Data Engineering / Data Analytics**

---

## 🧱 Estrutura do Projeto

```text
etl_selic/
├── data/
│   ├── raw/            # Dados brutos extraídos da fonte
│   └── processed/      # Dados tratados e prontos para análise
│
├── src/
│   ├── extract.py      # Extração dos dados
│   ├── transform.py   # Transformação dos dados
│   └── load.py        # (Opcional) Carga dos dados
│
├── README.md           # Documentação do projeto
└── requirements.txt   # Dependências do projeto




🛠️ Tecnologias Utilizadas

Python 3

Pandas

Requests

Git & GitHub

Conceitos de ETL / ELT



⚙️ Como Executar o Projeto

1️⃣ Clone o repositório

git clone https://github.com/manntanfumu0/etl-selic.git
cd etl-selic


2️⃣ Crie e ative o ambiente virtual (opcional)

python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows


3️⃣ Instale as dependências

pip install -r requirements.txt


4️⃣ Execute o pipeline

Extração
python src/extract.py


Transformação
python src/transform.py

Os dados brutos ficam em:
data/raw/

Os dados processados ficam em:
data/processed/


📈 Exemplo de Saída

Após a transformação, os dados ficam estruturados da seguinte forma:

data	valor
2016-02-01	14.25
2016-03-01	14.15


🧠 Aprendizados com o Projeto

Estruturação de pipelines de dados

Separação entre dados brutos e processados

Automação de ETL com Python

Versionamento de projetos com Git


🔮 Próximos Passos

Automatizar o pipeline com agendamento

Persistir dados em banco de dados (PostgreSQL)

Criar visualizações (Power BI ou Python)

Implementar testes de qualidade de dados

Containerizar o projeto com Docker


👨‍💻 Autor

Manuel Filipe Ntanfumu
Estudante de Tecnologia da Informação
Foco em Engenharia de Dados e Análise de Dados

📍 Brasil | Angola
🔗 GitHub: https://github.com/manntanfumu0
Organização profissional de repositórios de dados

