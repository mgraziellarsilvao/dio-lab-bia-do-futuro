# 🧠 Base de Conhecimento

---

## 📊 Dados Utilizados

O FinAI utiliza uma base simples e eficiente baseada em arquivos `.csv`, permitindo persistência e integração com ferramentas de análise.

| Arquivo | Formato | Utilização no Agente |
|---------|--------|---------------------|
| `transacoes.csv` | CSV | Armazena todas as transações financeiras registradas pelo usuário |

---

## 🔧 Adaptações nos Dados

O dataset foi criado e estruturado especificamente para o projeto, com foco em simplicidade e integração.

Adaptações realizadas:

- Padronização de colunas:
  - `data`
  - `descricao`
  - `categoria`
  - `valor`
  - `tipo`
- Definição de categorias fixas para evitar inconsistência
- Estrutura compatível com:
  - Pandas
  - Power BI
  - Excel

Não foram utilizados datasets externos, pois o objetivo é simular um ambiente real de entrada de dados pelo usuário.

---

## 🔗 Estratégia de Integração

### 📥 Como os dados são carregados?

Os dados são carregados a partir de um arquivo CSV utilizando a biblioteca Pandas.

- Se o arquivo existir → é carregado
- Se não existir → é criado automaticamente

```python
df = pd.read_csv("data/transacoes.csv")
