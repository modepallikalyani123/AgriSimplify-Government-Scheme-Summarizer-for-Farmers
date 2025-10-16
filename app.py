import streamlit as st
from googletrans import Translator
from summarize import simplify_text
import importlib.util
import importlib.machinery


st.set_page_config(page_title="AgriSimplify", layout="centered")
st.title("🌾 AgriSimplify: Government Scheme Summarizer for Farmers")
st.write("Simplify complex government scheme documents into 3–4 easy bullet points.")
# Input
text_input = st.text_area("Paste government scheme text here:", height=200)
if st.button("Simplify Text"):
    if text_input:
        with st.spinner("Simplifying..."):
            summary = simplify_text(text_input)
            st.subheader("Simplified Summary:")
            st.write("• " + summary.replace(". ", "\n• "))
    else:
        st.warning("Please enter some text to summarize.")

# Translation
st.subheader("Translate Summary:")
translator = Translator()
lang = st.selectbox("Choose Language", ["Telugu", "Hindi", "Tamil", "Kannada", "Malayalam"])
if st.button("Translate"):
    translated = translator.translate(summary, dest=lang.lower()[:2])
    st.success(translated.text)
