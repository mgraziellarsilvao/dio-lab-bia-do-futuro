# 📂 Exemplos de Uso - FinAI

Esta pasta contém demonstrações de como o assistente processa informações financeiras e as transforma em dados estruturados.

## 🤖 Casos de Uso (Input vs Output)

O FinAI utiliza Engenharia de Prompt para extrair entidades de frases informais. Abaixo estão exemplos de como a IA interpreta diferentes situações:

### 1. Registro de Despesa
**Entrada do Usuário:** > "Paguei 45 reais no almoço de hoje"

**Processamento Interno (JSON):**
```json
{
  "tipo_acao": "registro",
  "data": "2026-04-08",
  "descricao": "Almoço",
  "categoria": "alimentacao",
  "valor": 45.0,
  "tipo": "saida",
  "mensagem": "Registro de alimentação feito com sucesso!"
}
