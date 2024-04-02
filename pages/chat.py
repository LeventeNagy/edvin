import streamlit as st
import os
from supabase import create_client, Client
from data.knowledge import Knowledge
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

st.markdown("""
    <h1 style='text-align: center; color: gray;'>Edvin</h1>
    <p style='text-align: center; color: white; margin-top: -20px;'>Your licensing assistant</p>
    """, unsafe_allow_html=True)

claude = anthropic.Anthropic(
    api_key=os.environ["CLAUDE_API_KEY"]
)

sp = open("./system/system_prompt.txt", "r")
system_prompt = sp.read()

licensing = Knowledge.licensing()


prompt = st.chat_input()

if not prompt:
    with st.expander("Example questions"):
        st.write("What documents do I need to apply for a personal licence?")
        st.write("Provide me with a download link for a TEN application")
        st.write("Show me the map for Zone B")

if prompt:
    
    with st.spinner():

        message = claude.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1024,
            system=system_prompt,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        st.chat_message("user").markdown(prompt)
        st.chat_message("assistant").markdown(message.content[0].text, unsafe_allow_html=True)
