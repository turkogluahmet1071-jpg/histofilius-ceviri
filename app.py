import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları ve Eski Tasarım (Mermer Dokusu)
st.set_page_config(page_title="EPIGRAPHOS | Antik Yazıt Analizi", page_icon="🏛️", layout="wide")

# API Anahtarın
API_KEY = "AIzaSyBpuXwhUlhXcRd4eZ9Sp4uIL4LKfYsN8pg"

# Yapılandırma - EN SADE HALİ (v1beta falan yok!)
genai.configure(api_key=API_KEY)

# O Sevdiğin Antik Tasarım (CSS)
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/white-marble.png");
        background-color: #f4f1ea;
    }
    .stButton>button {
        background-color: #4a4a4a;
        color: white;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
    }
    h1 {
        color: #2c3e50;
        font-family: 'Georgia', serif;
        border-bottom: 3px solid #2c3e50;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🏛️ EPIGRAPHOS | Histofilius</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>Antik Epigrafi ve Metin Analiz Laboratuvarı</p>", unsafe_allow_html=True)

input_text = st.text_area("Antik Yazıt Metnini Buraya Girin:", placeholder="Örn: ΣΩΚΡΑΤΗΣ ΕΝ ΑΘΗΝΑΙΣ", height=150)

if st.button("Analiz Et"):
    if input_text:
        with st.spinner("Profesör metni inceliyor..."):
            try:
                # Modeli BURADA tanımlıyoruz (En stabil model)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = f"Sen uzman bir epigrafistsin. Şu antik metni akademik bir titizlikle analiz et: {input_text}"
                
                # Cevap üretme
                response = model.generate_content(prompt)
                
                st.success("Analiz Başarıyla Tamamlandı!")
                st.markdown("---")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Teknik bir aksaklık oldu: {e}")
    else:
        st.warning("Analiz için bir metin girmelisiniz.")
