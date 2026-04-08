# 📂 Exemplos de Uso e Demonstração - FinAI

Este documento apresenta como o assistente **FinAI** interpreta mensagens em linguagem natural e as converte em dados estruturados para controle financeiro.

---

## 🤖 Casos de Uso (Extração de Dados)

O FinAI utiliza Inteligência Artificial para identificar o valor, a descrição e a categoria correta, mesmo em frases informais.

---

### 1. 📉 Registro de Despesa (Saída)

**Usuário diz:**
> "Paguei 45 reais no almoço de hoje"

**Interpretação da IA (JSON):**

{
  "tipo_acao": "registro",
  "data": "2026-04-08",
  "descricao": "Almoço",
  "categoria": "alimentacao",
  "valor": 45.0,
  "tipo": "saida",
  "mensagem": "Registro de alimentação feito com sucesso! Bom apetite."
}

---

### 2. 📈 Registro de Receita (Entrada)

**Usuário diz:**
> "Recebi um bônus de 1500 reais"

**Interpretação da IA (JSON):**

{
  "tipo_acao": "registro",
  "data": "2026-04-08",
  "descricao": "Bônus",
  "categoria": "outros",
  "valor": 1500.0,
  "tipo": "entrada",
  "mensagem": "Excelente notícia! O valor já foi adicionado aos seus ganhos."
}

---

## 🗄️ Estrutura da Base de Dados

O FinAI utiliza o **Pandas** para gerenciar a persistência de dados. Todas as transações são consolidadas em um arquivo `.csv`, otimizado para integração com **Power BI** e **Excel**.

---

### 📊 Dicionário de Dados

| Campo        | Tipo        | Descrição |
|--------------|------------|----------|
| data         | Date       | Data da transação (YYYY-MM-DD) |
| descricao    | String     | Resumo da transação |
| categoria    | String     | Categoria padronizada |
| valor        | Float      | Valor monetário |
| tipo         | String     | entrada ou saida |

---

## ⚖️ Regras de Negócio

### 🧹 Categorização

Entradas:
- salario
- aluguel
- vendas
- outros

Saídas:
- aluguel
- moradia
- alimentacao
- lazer
- saude
- transporte

---

### 📅 Datas

- Se o usuário disser "ontem", o sistema calcula automaticamente  
- Se não disser nada, usa a data atual  

---

### 🧠 NLP

A IA retorna sempre dados estruturados (JSON), evitando erros e garantindo consistência.

---

### 💾 Persistência

- Os dados são salvos automaticamente no CSV  
- Não há perda de informação  
- Pode integrar direto com BI  

---

## 🚀 Integração

Compatível com:
- Power BI
- Excel

---

## 💡 Resumo

O FinAI atua como:
- Assistente financeiro
- Processador de linguagem natural
- Gerador de insights

---

Projeto desenvolvido para portfólio 🚀
