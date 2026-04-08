# 📘 Documentação do Agente

---

## 🧠 Caso de Uso

### 📌 Problema
Muitas pessoas não possuem controle claro sobre suas finanças pessoais, registrando gastos de forma desorganizada ou nem registrando.  
Além disso, interpretar valores e categorizar despesas manualmente é trabalhoso e sujeito a erros.

---

### 🚀 Solução
O FinAI resolve esse problema utilizando Inteligência Artificial para:

- Interpretar mensagens em linguagem natural
- Extrair automaticamente:
  - valor
  - descrição
  - categoria
  - tipo (entrada/saída)
- Estruturar os dados em formato JSON
- Armazenar automaticamente em um arquivo CSV

O agente atua de forma **proativa**, convertendo conversas em dados financeiros estruturados, sem necessidade de preenchimento manual.

---

### 🎯 Público-Alvo
- Pessoas que desejam organizar suas finanças pessoais
- Usuários iniciantes em controle financeiro
- Profissionais que querem integrar dados com Power BI ou Excel
- Usuários que preferem interação conversacional ao invés de planilhas

---

## 🤖 Persona e Tom de Voz

### Nome do Agente
**FinAI**

---

### 🧑‍💼 Personalidade
- Assistente financeiro inteligente
- Objetivo e eficiente
- Educativo e orientado a dados

---

### 💬 Tom de Comunicação
- Acessível
- Levemente informal
- Claro e direto

---

### 🗣️ Exemplos de Linguagem

- **Saudação:**  
  "Olá! Como posso te ajudar com suas finanças hoje?"

- **Confirmação:**  
  "Registro realizado com sucesso!"

- **Erro/Limitação:**  
  "Não consegui entender completamente. Pode reformular a frase?"

---

## 🏗️ Arquitetura

### 🔁 Diagrama

```mermaid
flowchart TD
    A[Usuário] -->|Mensagem| B[Streamlit]
    B --> C[Agente FinAI]
    C --> D[LLM Gemini 1.5]
    D --> C
    C --> E[Validação JSON]
    E --> F[DataFrame Pandas]
    F --> G[Arquivo CSV]
    G --> H[Resposta ao Usuário]
