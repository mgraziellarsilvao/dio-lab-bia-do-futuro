import streamlit as st
import pandas as pd
from src.agente import processar_conversa, carregar_dados

# --- CONFIGURAÇÃO DA PÁGINA E ESTILO (NÃO MUDA) ---
st.set_page_config(page_title="FinAI - Conversacional", layout="centered")

# Mantendo seu CSS original para cores e fundo
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
    }
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- INICIALIZAÇÃO DO ESTADO ---
# Removendo passo e buffer, mantendo apenas o histórico e os dados
if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {"role": "assistant", "content": "Olá! Sou o FinAI. O que vamos fazer hoje?"}
    ]

if "dados" not in st.session_state:
    st.session_state.dados = carregar_dados()

# --- TÍTULO ---
st.markdown("<h1 style='text-align: center; color: white;'>FinAI</h1>", unsafe_allow_html=True)

# --- EXIBIÇÃO DO CHAT ---
for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

# --- INPUT DO USUÁRIO ---
if prompt := st.chat_input("Digite aqui..."):
    # Adiciona a mensagem do usuário ao histórico e exibe
    st.session_state.mensagens.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # CHAMA O NOVO CÉREBRO (IA GENERATIVA)
    # Passamos o texto e o dataframe atual. Ele retorna a resposta e o df atualizado
    resposta, df_atualizado = processar_conversa(prompt, st.session_state.dados)
    
    # Atualiza o estado global com os novos dados
    st.session_state.dados = df_atualizado

    # Adiciona a resposta do FinAI ao histórico e exibe
    st.session_state.mensagens.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.write(resposta)

# --- BOTÃO DE LIMPEZA (OPCIONAL) ---
if st.sidebar.button("Limpar Conversa"):
    st.session_state.mensagens = [{"role": "assistant", "content": "Olá! Sou o FinAI. O que vamos fazer hoje?"}]
    st.rerun()