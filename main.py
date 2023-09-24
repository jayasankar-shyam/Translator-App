import streamlit as st
import requests
from googletrans import Translator,LANGUAGES

st.title("Language Translator App")

user_input = st.text_area("Enter the text to translate:")

source_language = st.selectbox("Select the source language:", list(LANGUAGES.values()),index=21) 
target_language = st.selectbox("Select the target language:", list(LANGUAGES.values()),index=62) 

def translate_text(text,source,target):
  trans = Translator()
  translation = trans.translate(text,src=source,dest=target)
  return translation.text

if st.button("Translate"):
    if user_input:
        translation = translate_text(user_input, source_language, target_language)
        st.success(f"Translation: {translation}")
    else:
        st.warning("Please try again.")
