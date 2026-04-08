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
