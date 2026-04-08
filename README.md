# 💰 FinAI - Assistente de Gestão Financeira com IA

O FinAI é um agente inteligente desenvolvido para simplificar o registro de transações financeiras usando Linguagem Natural. 

## 🚀 Funcionalidades
- **Processamento de Linguagem Natural**: Transforma frases como "Gastei 50 reais com pizza" em registros estruturados.
- **Base de Dados Dinâmica**: Armazenamento automático em CSV via Pandas.
- **Categorização Inteligente**: Baseada em regras de negócio rígidas.

## 🛠️ Tecnologias
- **Python 3.10+**
- **Streamlit** (Interface)
- **Google Gemini API** (Cérebro do Agente)
- **Pandas** (Tratamento de dados)

## 📋 Como rodar
1. Clone o repositório.
2. Crie um arquivo `.streamlit/secrets.toml` com sua `GOOGLE_API_KEY`.
3. Instale as dependências: `pip install -r requirements.txt`.
4. Execute: `streamlit run app.py`.
