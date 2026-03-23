import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="EPIGRAPHOS | Antik Yazıt Analizi", page_icon="🏛️", layout="wide")

# API Anahtarın (Buraya kendi anahtarını tırnak içinde koy)
API_KEY = "AIzaSyBpuXwhUlhXcRd4eZ9Sp4uIL4LKfYsN8pg"

# Google AI Yapılandırması (En sade hali)
genai.configure(api_key=API_KEY)

# Tasarım (CSS)
st.markdown("""
    <style>
    .main { background-color: #f4f1ea; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #4a4a4a; color: white; }
    .reportview-container .main .block-container { padding-top: 2rem; }
    h1 { color: #2c3e50; font-family: 'Georgia', serif; border-bottom: 2px solid #2c3e50; padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🏛️ EPIGRAPHOS | Histofilius</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Antik Epigrafi ve Metin Analiz Laboratuvarı</p>", unsafe_allow_html=True)

# Kullanıcı Girişi
input_text = st.text_area("Antik Yazıt Metnini Buraya Girin (Grekçe veya Latince):", placeholder="Örn: ΣΩΚΡΑΤΗΣ ΕΝ ΑΘΗΝΑΙΣ", height=150)

if st.button("Analiz Et"):
    if input_text:
        with st.spinner("Profesör analiz ediyor, lütfen bekleyin..."):
            try:
                # En güncel ve stabil model
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = f"Sen uzman bir epigrafistsin. Şu antik metni analiz et: {input_text}. Sonucu şu başlıklarla ver: 1- Diplomatik Transkripsiyon, 2- Türkçe Çeviri, 3- Tarihsel ve Epigrafik Yorum."
                
                response = model.generate_content(prompt)
                
                st.success("Analiz Tamamlandı!")
                st.markdown("### 📜 Analiz Sonuçları")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Bir hata oluştu: {e}")
    else:
        st.warning("Lütfen bir metin girin.")
