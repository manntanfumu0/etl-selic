# ETL SELIC – Data Engineering Project

Pipeline de dados desenvolvido em **Python** para extração, transformação e organização da taxa **SELIC**, seguindo boas práticas de **Engenharia de Dados** e estruturação de projetos analíticos.

Projeto voltado para portfólio de **Data Engineer / Data Analyst Júnior**.

---

## 🎯 Objetivo

- Construir um pipeline ETL simples e funcional
- Extrair dados de fonte pública
- Transformar e padronizar dados para uso analítico
- Organizar dados no padrão **raw → processed**
- Demonstrar boas práticas de versionamento e organização

---

## 🗂 Estrutura do Projeto

```text
etl_selic/
├── data/
│   ├── raw/            # Dados brutos
│   └── processed/      # Dados tratados
│
├── src/
│   ├── extract.py      # Extração dos dados
│   ├── transform.py   # Transformação dos dados
│   └── load.py        # (Opcional) Carga
│
├── README.md
└── requirements.txt


---

🛠 Tecnologias

Python 3

Pandas

Requests

Git & GitHub

Conceitos de ETL / ELT


---

▶️ Execução

git clone https://github.com/manntanfumu0/etl-selic.git
cd etl-selic
pip install -r requirements.txt
python src/extract.py
python src/transform.py

Saídas:

Dados brutos: data/raw/
Dados processados: data/processed/



📊 Exemplo de Resultado
data	valor
2016-02-01	14.25
2016-03-01	14.15


---

🧠 Principais Aprendizados

- Construção de pipelines ETL
- Organização de projetos de dados
- Separação de dados brutos e tratados
- Automação com Python
- Versionamento com Git

---

🚀 Próximas Evoluções

* Persistência em banco de dados (PostgreSQL)
* Agendamento do pipeline
* Testes de qualidade de dados
* Visualização analítica
* Dockerização

---


👤 Autor

Manuel Filipe Ntanfumu
Estudante de Tecnologia da Informação
Foco em Engenharia de Dados e Análise de Dados

📍 Brasil | Angola
🔗 GitHub: https://github.com/manntanfumu0

