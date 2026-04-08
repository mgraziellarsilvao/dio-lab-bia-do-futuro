# 📊 Avaliação e Métricas

---

## 🧪 Como Avaliar o Agente

A avaliação do FinAI foi realizada através de testes estruturados simulando interações reais com o usuário.

O foco foi validar:

- Extração correta de dados
- Estrutura JSON consistente
- Respostas fora de escopo
- Comportamento em cenários ambíguos

---

## 📈 Métricas de Qualidade

| Métrica | O que avalia | Aplicação no FinAI |
|--------|-------------|-------------------|
| **Assertividade** | Capacidade de extrair corretamente os dados | Identificação de valor, categoria e tipo |
| **Segurança** | Evita inventar informações | Uso de JSON estruturado e categorias fixas |
| **Coerência** | Respostas fazem sentido no contexto financeiro | Classificação correta de entrada/saída |

---

## 🧪 Cenários de Teste

### ✅ Teste 1: Registro de despesa

- **Pergunta:** "Paguei 50 reais no mercado"
- **Resultado esperado:** Registro com categoria `alimentacao`
- **Resultado:** [x] Correto  [ ] Incorreto

---

### ✅ Teste 2: Registro de receita

- **Pergunta:** "Recebi 2000 de salário"
- **Resultado esperado:** Registro com tipo `entrada`
- **Resultado:** [x] Correto  [ ] Incorreto

---

### ✅ Teste 3: Pergunta fora do escopo

- **Pergunta:** "Qual a previsão do tempo?"
- **Resultado esperado:** Resposta informando limitação do agente
- **Resultado:** [x] Correto  [ ] Incorreto

---

### ⚠️ Teste 4: Frase ambígua

- **Pergunta:** "Gastei um pouco ontem"
- **Resultado esperado:** Dificuldade de interpretação ou erro controlado
- **Resultado:** [ ] Correto  [x] Incorreto

---

## 📊 Resultados

### ✅ O que funcionou bem

- Extração de valores numéricos com alta precisão  
- Classificação correta entre entrada e saída  
- Estrutura JSON consistente  
- Persistência automática no CSV  
- Respostas fora do escopo bem controladas  

---

### ⚠️ O que pode melhorar

- Interpretação de frases vagas ou incompletas  
- Tratamento de múltiplas transações em uma única frase  
- Melhor entendimento de contexto temporal (ex: "semana passada")  
- Feedback mais detalhado ao usuário em caso de erro  

---

## 🚀 Métricas Avançadas

Mesmo não utilizando ferramentas externas de observabilidade, o projeto apresenta:

- Baixa latência (respostas rápidas com Gemini Flash)
- Baixo custo computacional (uso eficiente de tokens)
- Tratamento de erros com try/except

---

## 💡 Conclusão

O FinAI apresentou bom desempenho nos testes principais, com destaque para:

- Confiabilidade na estrutura dos dados
- Baixo nível de alucinação
- Simplicidade e eficiência na arquitetura

---

Projeto validado com foco em robustez e evolução contínua 🚀
