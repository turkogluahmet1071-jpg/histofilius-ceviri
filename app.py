import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="EPIGRAPHOS | Antik Yazıt Analizi", layout="wide")

# --- CSS: LACİVERT & GRİ TEMAYI KORU ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stTextArea textarea { border: 2px solid #1a2a3a; border-radius: 10px; }
    .header-box {
        background-color: #1a2a3a;
        padding: 40px;
        border-radius: 15px;
        color: white;
        text-align: left;
        margin-bottom: 25px;
        border-bottom: 5px solid #c5a059;
    }
    .info-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        height: 100%;
        border-top: 4px solid #1a2a3a;
    }
    .dictionary-item {
        background-color: #f1f3f5;
        padding: 8px;
        border-radius: 5px;
        margin-bottom: 5px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 0.9em;
    }
    </style>
    """, unsafe_allow_html=True)

# --- API AYARI ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("API Anahtarı bulunamadı! Lütfen Secrets kısmını kontrol edin.")

# --- HEADER ---
st.markdown("""
    <div class="header-box">
        <h1 style='margin:0; font-family: serif; letter-spacing: 2px;'>EPIGRAPHOS</h1>
        <p style='margin:5px 0 0 0; opacity: 0.8;'>ANTİK YUNAN YAZIT ANALİZ LABORATUVARI</p>
        <p style='text-align:right; font-style: italic; color:#c5a059;'> "Scripta manent, verba volant."</p>
    </div>
    """, unsafe_allow_html=True)

# --- ÜST BİLGİ ALANI (3 KOLON) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="info-card">
            <h4 style="color:#1a2a3a;">⚒️ Metodoloji</h4>
            <p style="font-size:0.9em; color:#666;">
            > Leiden Konvansiyonu kullanımı<br>
            > Paleografik karşılaştırma<br>
            > Onomastik veritabanı taraması
            </p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="info-card">
            <h4 style="color:#1a2a3a;">📖 Epigrafi Sözlüğü</h4>
            <div class="dictionary-item"><b>Boustrophedon:</b> Öküz dönüşü yazım stili.</div>
            <div class="dictionary-item"><b>Stela:</b> Dikili taş, yazıt levhası.</div>
            <div class="dictionary-item"><b>Votif:</b> Adak yazıtı, tanrılara sunu.</div>
            <div class="dictionary-item"><b>Onomastik:</b> İsim bilimi çalışması.</div>
        </div>
        """, unsafe_allow_html=True)

with col3:
    st.markdown('<div class="info-card"><h4 style="color:#1a2a3a;">🎙️ Histofilius Podcast</h4>', unsafe_allow_html=True)
    # Spotify Embed Player (Doğrudan Bölüm Oynatıcı)
    st.markdown("""
        <iframe style="border-radius:12px" 
        src="https://open.spotify.com/embed/episode/5678" 
        width="100%" height="152" frameBorder="0" allowfullscreen="" 
        allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- ANALİZ ALANI ---
st.subheader("🖋️ Analiz Edilecek Metni Girin")
input_text = st.text_area("", placeholder="Örn: ΣΩΚΡΑΤΗΣ EN ΑΘΗΝΑİΣ", height=150)

if st.button("ANALİZİ BAŞLAT", use_container_width=True):
    if input_text:
        with st.spinner("Profesör Gemini 2.0 kütüphaneden geliyor... 🏛️"):
            try:
                # Modeli çağırıyoruz
                model = genai.GenerativeModel('gemini-2.0-flash')
                
                prompt = f"""
                Sen uzman bir epigrafistsin. Aşağıdaki antik metni akademik bir titizlikle analiz et:
                Metin: {input_text}
                
                Lütfen şu formatta cevap ver:
                1. Transkripsiyon (Grekçe/Latince)
                2. Türkçe Çeviri
                3. Tarihsel ve Epigrafik Yorum (Kısa ve öz)
                """
                
                response = model.generate_content(prompt)
                
                st.success("Analiz Tamamlandı!")
                st.markdown("### 📜 Profesörün Notları")
                st.info(response.text)
                
            except Exception as e:
                if "429" in str(e):
                    st.error("⚠️ Kota doldu. Lütfen 1 dakika bekleyip tekrar deneyin.")
                else:
                    st.error(f"Teknik bir durum: {e}")
    else:
        st.warning("Lütfen analiz edilecek bir metin girin.")
