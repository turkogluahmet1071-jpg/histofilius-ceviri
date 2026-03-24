import streamlit as st
import google.generativeai as genai
# PIL kütüphanesini (Pillow) logo işlemek için kullanıyoruz
from PIL import Image

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="EPIGRAPHOS | Antik Yazıt Analizi", layout="wide")

# --- CSS: TASARIM VE RENK PALETİ ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; } /* Hafif gri arka plan */
    .stTextArea textarea { border: 2px solid #1a2a3a; border-radius: 10px; }
    
    /* LACİVERT HEADER VE ANTİK SEMBOLLER */
    .header-box {
        background-color: #1a2a3a; /* Oxford Mavisi */
        padding: 40px;
        border-radius: 15px;
        color: white;
        text-align: left;
        margin-bottom: 25px;
        border-bottom: 8px solid #c5a059; /* Altın Sarısı Vurgu */
        
        /* Arka plana antik semboller (Meander motifi) işliyoruz */
        background-image: url('https://googleusercontent.com/images?q=tbn:ANd9GcR_xQy_XpG9L7Z1N5tB3L9QvY8J1H9E7w');
        background-repeat: repeat-x;
        background-position: bottom;
        background-size: 50px;
    }
    
    /* BİLGİ KARTLARI TASARIMI */
    .info-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 6px 10px rgba(0,0,0,0.15);
        height: 100%;
        border-top: 5px solid #1a2a3a;
        transition: transform 0.2s; /* Hafif hover efekti */
    }
    .info-card:hover { transform: translateY(-3px); }
    
    .dictionary-item {
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 8px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 0.95em;
        border-left: 3px solid #c5a059;
    }
    </style>
    """, unsafe_allow_html=True)

# --- API AYARI (Değişmedi) ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("API Anahtarı bulunamadı! Lütfen Secrets kısmını kontrol edin.")

# --- HEADER: SEMBOLLÜ VE ASİL ---
st.markdown("""
    <div class="header-box">
        <h1 style='margin:0; font-family: serif; letter-spacing: 3px; font-size: 3em;'>EPIGRAPHOS 🏛️</h1>
        <p style='margin:10px 0 0 0; opacity: 0.9; font-size: 1.2em;'>ANTİK YUNAN YAZIT ANALİZ LABORATUVARI</p>
        <p style='text-align:right; font-style: italic; color:#c5a059; margin-top: -10px;'> "Scripta manent, verba volant."</p>
    </div>
    """, unsafe_allow_html=True)

# --- ÜST BİLGİ ALANI (3 KOLON) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="info-card">
            <h3 style="color:#1a2a3a; border-bottom: 2px solid #c5a059; padding-bottom:10px;">⚒️ Metodoloji</h3>
            <p style="font-size:1em; color:#555; line-height: 1.6;">
            > Leiden Konvansiyonu kullanımı<br>
            > Paleografik karşılaştırma<br>
            > Onomastik veritabanı taraması
            </p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="info-card">
            <h3 style="color:#1a2a3a; border-bottom: 2px solid #c5a059; padding-bottom:10px;">📖 Epigrafi Sözlüğü</h3>
            <div class="dictionary-item"><b>Boustrophedon:</b> Öküz dönüşü yazım stili.</div>
            <div class="dictionary-item"><b>Stela:</b> Dikili taş, yazıt levhası.</div>
            <div class="dictionary-item"><b>Votif:</b> Adak yazıtı, tanrılara sunu.</div>
            <div class="dictionary-item"><b>Onomastik:</b> İsim bilimi çalışması.</div>
        </div>
        """, unsafe_allow_html=True)

with col3:
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#1a2a3a; text-align:center;">🎙️ Histofilius</h3>', unsafe_allow_html=True)
    
    # --- LOGO OPERASYONU ---
    # Spotify yerine senin o efsane logon gelecek.
    # Lütfen 'logo.png' dosyasını GitHub'daki 'app.py' ile aynı klasöre yükle!
    try:
        logo_image = Image.open('logo.png')
        # Logoyu kartın ortasına ve şık bir boyutta koyuyoruz
        st.image(logo_image, width=180, use_container_width=False, output_format="PNG")
    except:
        st.warning("⚠️ logo.png bulunamadı! Lütfen GitHub'a yükleyin.")
        
    st.markdown("""
        <p style="font-size:0.9em; color:#666; text-align:center; margin-top:10px;">
        Antik dünyayı Histofilius ile keşfedin.
        </p>
        <div style="text-align:center; margin-top:15px;">
            <a href="http://googleusercontent.com/spotify.com/6" target="_blank" 
               style="background-color: #c5a059; color: #1a2a3a; padding: 10px 20px; text-radius: 25px; text-decoration: none; font-weight: bold; border-radius: 20px;">
               Bölümleri Dinle
            </a>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

# --- ANALİZ ALANI (Gemini 2.0 Hazır, Yarını Bekliyor) ---
st.subheader("🖋️ Analiz Edilecek Metni Girin")
input_text = st.text_area("", placeholder="Örn: ΣΩΚΡΑΤΗΣ EN ΑΘΗΝΑİΣ", height=150)

if st.button("ANALİZİ BAŞLAT", use_container_width=True):
    if input_text:
        # Kota bugünlük dolduğu için profesör çay molasında ☕
        st.error("⚠️ Profesör Gemini bugünlük kütüphaneyi kapattı (Kota Doldu). Lütfen yarına kadar antik metinlerinizi saklayın. 🏛️😴")
    else:
        st.warning("Lütfen bir metin girin.")
