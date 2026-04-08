import os
import json
import pandas as pd
from datetime import datetime
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Configuração (COLE SUA CHAVE NOVA AQUI)
os.environ["GOOGLE_API_KEY"] = ["GOOGLE_API_KEY"]

# 2. Inicializa o modelo de forma estável
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

CATEGORIAS_GANHO = ["salario", "aluguel", "vendas", "outros"]
CATEGORIAS_DESPESA = ["aluguel", "moradia", "alimentacao", "lazer", "saude", "transporte"]

def carregar_dados():
    caminho = "data/transacoes.csv"
    if not os.path.exists("data"): os.makedirs("data")
    if os.path.exists(caminho): return pd.read_csv(caminho)
    return pd.DataFrame(columns=["data", "descricao", "categoria", "valor", "tipo"])

def processar_conversa(texto, df):
    prompt_sistema = f"""Você é o FinAI. Extraia dados de transações.
    Categorias: Ganho{CATEGORIAS_GANHO}, Despesa{CATEGORIAS_DESPESA}.
    Responda APENAS JSON: {{"tipo_acao": "registro", "data": "AAAA-MM-DD", "descricao": "...", "categoria": "...", "valor": 0.0, "tipo": "entrada/saida", "mensagem": "..."}}
    Se for conversa, use "tipo_acao": "conversa"."""

    try:
        # Chamada via LangChain (evita o erro 404 de v1beta)
        response = model.invoke(prompt_sistema + "\nUsuário: " + texto)
        
        conteudo = response.content.replace('```json', '').replace('```', '').strip()
        res_json = json.loads(conteudo)
        
        if res_json.get("tipo_acao") == "registro":
            nova_linha = {
                "data": res_json["data"], "descricao": res_json["descricao"],
                "categoria": res_json["categoria"], "valor": res_json["valor"], "tipo": res_json["tipo"]
            }
            novo_df = pd.concat([df, pd.DataFrame([nova_linha])], ignore_index=True)
            novo_df.to_csv("data/transacoes.csv", index=False)
            return res_json["mensagem"], novo_df
        
        return res_json.get("mensagem", "Entendi!"), df
    except Exception as e:
        return f"Erro de conexão: {str(e)}", df