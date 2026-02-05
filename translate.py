import streamlit as st
from googletrans import Translator,LANGUAGES
import asyncio

st.header("Translate Text",divider="rainbow")
translator = Translator(service_urls=[
    'translate.googleapis.com'
    ])

# language_map
LANGUAGE_MAP = LANGUAGES

name = {name.title() : code for code,name in LANGUAGE_MAP.items() }
LANG =  list(name.keys())
SOURCE_LANGS = ["Auto detect"] + list(name.keys())
TARGET_LANGS = list(name.keys())

if "output" not in st.session_state:
    st.session_state.output = ""

async def translate(message: str, language : str= "English"):
    translated_result = await translator.translate(message, dest=name[language])
    return translated_result.text
    


col1,col2 = st.columns(2)
output = ""
with col1:
    
    txt = st.selectbox(label="language",options=SOURCE_LANGS)
    message = st.text_area(label="Input text",placeholder="Enter text here",label_visibility="collapsed",height=300)
    
        
with col2:
    txt1 = st.selectbox(label="Select language",options=TARGET_LANGS)
if st.button(label="Generate"):
    if message.strip():
        with st.spinner("Translating..."):
            st.session_state.output = asyncio.run(
                translate(message, txt1)
            )
with col2:
    st.text_area(
        label="Output",
        height=300,
        key="output",
        disabled=True
    )

st.subheader("List of languages", divider="rainbow")

st.write(LANGUAGES)