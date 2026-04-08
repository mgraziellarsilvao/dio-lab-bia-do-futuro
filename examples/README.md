# 📂 Exemplos de Uso e Demonstração - FinAI

Este documento apresenta como o assistente **FinAI** interpreta mensagens em linguagem natural e as converte em dados estruturados para controle financeiro.

## 🤖 Casos de Uso (Extração de Dados)

O FinAI utiliza Inteligência Artificial para identificar o valor, a descrição e a categoria correta, mesmo em frases informais.

### 1. Registro de Despesa (Saída)
**Usuário diz:** > *"Paguei 45 reais no almoço de hoje"*

**Interpretação da IA (JSON):**
```json
{
  "tipo_acao": "registro",
  "data": "2026-04-08",
  "descricao": "Almoço",
  "categoria": "alimentacao",
  "valor": 45.0,
  "tipo": "saida",
  "mensagem": "Registro de alimentação feito com sucesso! Bom apetite."
}
### 2. Registro de Receita (Entrada)
Usuário diz: > "Recebi um bônus de 1500 reais"*

**Interpretação da IA (JSON):**
```json
{
  "tipo_acao": "registro",
  "data": "2026-04-08",
  "descricao": "Bônus",
  "categoria": "outros",
  "valor": 1500.0,
  "tipo": "entrada",
  "mensagem": "Excelente notícia! O valor já foi adicionado aos seus ganhos."
}

## 🗄️ Estrutura da Base de Dados

O FinAI utiliza o **Pandas** para gerenciar a persistência de dados. Todas as transações são consolidadas em um arquivo flat-file (`.csv`), otimizado para integração direta com ferramentas de visualização como **Power BI** e **Excel**.

### Dicionário de Dados
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `data` | Date (ISO) | Data da transação no formato YYYY-MM-DD. |
| `descricao` | String | Breve resumo da transação extraído pela IA. |
| `categoria` | String | Categoria padronizada conforme regras de negócio. |
| `valor` | Float | Valor monetário da transação (ex: 150.50). |
| `tipo` | String | Classificação binária: `entrada` ou `saida`. |

---

## ⚖️ Regras de Negócio e Lógica do Agente

Para garantir a qualidade dos dados (Data Integrity) e evitar inconsistências em relatórios financeiros, o agente segue diretrizes rígidas de processamento:

### 1. Categorização Padronizada (Data Cleaning)
A IA é instruída a classificar cada transação em um conjunto pré-definido de categorias. Se a entrada não se encaixar claramente, ela utiliza a categoria `outros`.

* **Fluxos de Ganho (Entrada):** `salario`, `aluguel`, `vendas`, `outros`.
* **Fluxos de Gasto (Saída):** `aluguel`, `moradia`, `alimentacao`, `lazer`, `saude`, `transporte`.

### 2. Inteligência de Datas (Time Intelligence)
* **Data Explícita:** Se o usuário disser "Ontem gastei...", a IA calcula a data correta.
* **Data Implícita:** Caso não haja menção temporal, o sistema utiliza automaticamente a data atual do servidor (`datetime.now()`).

### 3. Extração via NLP (Natural Language Processing)
O motor do Gemini 1.5 é configurado para retornar **estritamente um JSON**. Isso elimina ruídos na comunicação e garante que apenas dados estruturados sejam enviados para a função de concatenação do DataFrame.

### 4. Persistência e Backup
A cada novo registro validado, o sistema realiza o `commit` automático para o arquivo CSV, garantindo que não haja perda de dados em caso de encerramento da sessão do Streamlit.
