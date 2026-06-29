import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile
import pyperclip

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# ---------------- LANGUAGE DICTIONARY ----------------
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Bengali": "bn",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Arabic": "ar"
}

# ---------------- SESSION STATE ----------------
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

# ---------------- TITLE ----------------
st.title("🌍 AI Language Translation Tool")
st.write("Translate text between multiple languages.")

# ---------------- INPUT ----------------
text = st.text_area(
    "Enter Text",
    height=150,
    placeholder="Type your text here..."
)

# ---------------- LANGUAGE SELECTION ----------------
col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "Source Language",
        list(languages.keys()),
        index=0
    )

with col2:
    target = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=2
    )

# ---------------- TRANSLATE ----------------
if st.button("🌐 Translate"):

    if text.strip() == "":
        st.warning("Please enter text.")
    else:
        try:
            translated = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

            st.session_state.translated_text = translated

        except Exception as e:
            st.error("Translation Failed")
            st.write(e)

# ---------------- OUTPUT ----------------
if st.session_state.translated_text != "":

    st.subheader("Translated Text")

    st.text_area(
        "",
        value=st.session_state.translated_text,
        height=150
    )

    c1, c2, c3 = st.columns(3)

    # COPY
    with c1:
        if st.button("📋 Copy"):
            try:
                pyperclip.copy(st.session_state.translated_text)
                st.success("Copied Successfully")
            except:
                st.error("Copy Failed")

    # SPEAK
    with c2:
        if st.button("🔊 Speak"):
            try:
                tts = gTTS(
                    text=st.session_state.translated_text,
                    lang=languages[target]
                )

                file = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".mp3"
                )

                tts.save(file.name)

                st.audio(file.name)

            except:
                st.error("Speech not available for this language.")

    # CLEAR
    with c3:
        if st.button("🗑 Clear"):
            st.session_state.translated_text = ""
            st.rerun()

st.markdown("---")
st.markdown(
    "<center><b>Made with ❤️ using Streamlit + Deep Translator</b></center>",
    unsafe_allow_html=True
)
