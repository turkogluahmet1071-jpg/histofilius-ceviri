import streamlit as st
# import google.generativeai as genai  # GEMINI GEÇİCİ OLARAK KAPATILDI (Hata Almamak İçin)

# Sayfa Ayarları (Sadece Tasarım)
st.set_page_config(page_title="EPIGRAPHOS | Antik Yazıt Analizi", page_icon="🏛️", layout="wide")

# API Anahtarı (Bu kodda kullanılmayacak, sadece tasarım var)
# API_KEY = "AIzaSyBpuXwhUlhXcRd4eZ9Sp4uIL4LKfYsN8pg"

# Yapılandırma (GEMINI KAPATILDIĞI İÇİN BU KISMI ATLASSAK OLUR, AMA KODDA DURSUN)
# genai.configure(api_key=API_KEY)

# 🏛️ İŞTE MERMER DOKULU ANTİK TASARIM (CSS)
st.markdown("""
    <style>
    /* Ana Arka Plan: Mermer Dokusu */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/white-marble.png");
        background-color: #f4f1ea; /* Hafif Parşömen Tonu */
    }

    /* Başlık Alanı ve Roma Kırmızısı Çizgi */
    h1 {
        color: #8B0000; /* Pompeii Kırmızısı / Roma Kırmızısı */
        font-family: 'Georgia', serif;
        font-weight: bold;
        text-align: center;
        border-bottom: 3px solid #8B0000;
        padding-bottom: 15px;
        margin-top: 2rem;
    }

    /* Alt Başlıklar */
    h3 {
        color: #2c3e50;
        font-family: 'Times New Roman', serif;
        font-weight: normal;
        margin-top: 20px;
    }

    /* Metin Alanı ve Scroll Tasarımı */
    .stTextArea>div>div>textarea {
        background-color: rgba(255, 255, 255, 0.7); /* Hafif Şeffaf */
        border: 2px solid #2c3e50;
        border-radius: 10px;
        font-family: 'Courier New', monospace; /* Epigrafiye Uygun */
        font-size: 1.1em;
        color: #1a1a1a;
    }

    /* 📜 ANALİZ BUTONU (Bronz ve Asil) */
    .stButton>button {
        background-color: #b8860b; /* Koyu Bronz Renk */
        color: white;
        border-radius: 15px;
        height: 3.5em;
        width: 100%;
        font-weight: bold;
        font-size: 1.2em;
        border: 2px solid #8b6508;
        transition: 0.3s;
    }
    
    /* Butonun Üstüne Gelince */
    .stButton>button:hover {
        background-color: #cd853f; /* Biraz Daha Açık Bronz */
        color: #1a1a1a;
        border: 2px solid #cd853f;
    }

    /* Sonuç Kutusu Tasarımı */
    .stAlert {
        background-color: rgba(255, 255, 255, 0.9);
        border: 2px solid #2c3e50;
        color: #2c3e50;
        font-family: 'Georgia', serif;
    }

    </style>
    """, unsafe_allow_html=True)

# 🏛️ SAYFA BAŞLIĞI VE LOGO
st.markdown("<h1>🏛️ EPIGRAPHOS | Histofilius</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; color: #555;'>Antik Epigrafi ve Metin Analiz Laboratuvarı</p>", unsafe_allow_html=True)
st.markdown("---")

# ✍️ KULLANICI GİRİŞ ALANI
input_text = st.text_area("Antik Yazıt Metnini Buraya Girin (Grekçe veya Latince):", placeholder="Örn: ΣΩΚΡΑΤΗΣ ΕΝ ΑΘΗΝΑΙΣ", height=150)

# 📜 ANALİZ ET BUTONU
if st.button("Analiz Et"):
    if input_text:
        # Analiz Başlıyor ( Spinner da tasarımın bir parçası)
        with st.spinner("Profesör analiz ediyor, lütfen bekleyin... 🏛️⌛"):
            # try:
                # GEMINI GEÇİCİ OLARAK KAPATILDI
                # model = genai.GenerativeModel('gemini-1.5-flash')
                # prompt = f"Sen uzman bir epigrafistsin. Şu antik metni analiz et: {input_text}. Sonucu şu başlıklarla ver: 1- Diplomatik Transkripsiyon, 2- Türkçe Çeviri, 3- Tarihsel ve Epigrafik Yorum."
                # response = model.generate_content(prompt)
                
                # st.success("Analiz Tamamlandı!")
                # st.markdown("### 📜 Analiz Sonuçları")
                # st.write(response.text)
                
            # except Exception as e:
                # st.error(f"Teknik bir aksaklık oldu (404-v1beta): {e}")
                
            # TASARIMIN KALMASI İÇİN GEÇİCİ CEVAP
            st.info("⚠️ Profesör bugün izinli (Gemini 404 Hatası). Tasarımı görmektesiniz, analiz motoru daha sonra devreye girecektir. Girilen metin: " + input_text)
                
    else:
        st.warning("Analiz için bir metin girmelisiniz.")

# 👇 ALT BİLGİ VE İMZA (Opsiyonel)
st.markdown("<br><br><p style='text-align: center; color: #888;'>Histofilius | Antik Dünya Dijital Asistanı © 2024</p>", unsafe_allow_html=True)
            
