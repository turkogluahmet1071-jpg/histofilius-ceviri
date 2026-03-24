import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# --- 1. SAYFA YAPILANDIRMASI ---
st.set_page_config(page_title="EPIGRAPHOS | Analiz Laboratuvarı", layout="wide", initial_sidebar_state="collapsed")

# --- 2. GELİŞMİŞ CSS (React Görselliğini Aktarma) ---
st.markdown("""
    <style>
    /* Ana Arka Plan */
    .stApp { background-color: #fcfaf2; color: #2c2c2c; font-family: 'Georgia', serif; }
    
    /* Akademik Header */
    .header-box {
        background-color: #1a2a44;
        padding: 40px;
        border-radius: 0px 0px 20px 20px;
        color: #e5d5b0;
        border-bottom: 6px solid #8b7355;
        margin: -60px -100px 30px -100px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        text-align: center;
    }
    
    /* Kart Tasarımları (React stili gölgeli beyaz kartlar) */
    .info-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #e2e2e2;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    /* Buton ve Input Stil */
    .stButton>button {
        background-color: #8b7355 !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 15px !important;
        font-weight: bold !important;
        border: none !important;
        transition: 0.3s !important;
        width: 100%;
    }
    .stButton>button:hover { background-color: #6d5a43 !important; transform: translateY(-2px); }
    
    /* Sözlük Öğeleri */
    .dict-item {
        background-color: #f4f1ea;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 10px;
        border-left: 4px solid #8b7355;
        font-size: 0.9em;
    }

    /* Tab Stilini Özelleştirme */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 10px 10px 0px 0px;
        padding: 10px 20px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. API & LOGO HAZIRLIĞI ---
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except:
    st.error("API Anahtarı bulunamadı!")

# --- 4. HEADER ---
st.markdown("""
    <div class="header-box">
        <h1 style='letter-spacing: 5px; font-size: 3.5em; margin:0;'>EPIGRAPHOS</h1>
        <p style='text-transform: uppercase; letter-spacing: 2px; opacity: 0.8;'>Antik Yunan Yazıt Analiz Laboratuvarı</p>
        <p style='font-style: italic; color: #8b7355; margin-top:10px;'> "Scripta manent, verba volant."</p>
    </div>
    """, unsafe_allow_html=True)

# --- 5. ANA LAYOUT (3 KOLON: Sidebars & Content) ---
col_side, col_main = st.columns([1, 3], gap="large")

with col_side:
    # Metodoloji Kartı
    st.markdown("""
        <div class="info-card">
            <h4 style="color:#1a2a44; border-bottom: 2px solid #8b7355; padding-bottom: 5px;">⚖️ Metodoloji</h4>
            <ul style="font-size: 0.85em; padding-left: 15px; color: #555; margin-top: 10px;">
                <li>Leiden Konvansiyonu</li>
                <li>Paleografik Karşılaştırma</li>
                <li>Onomastik Tarama</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Sözlük Kartı
    st.markdown('<div class="info-card"><h4 style="color:#1a2a44; border-bottom: 2px solid #8b7355; padding-bottom: 5px;">📖 Sözlük</h4>', unsafe_allow_html=True)
    st.markdown('<div class="dict-item"><b>ΕΝΘΑΔΕ ΚΕΙΤΑΙ:</b> Burada yatıyor...</div>', unsafe_allow_html=True)
    st.markdown('<div class="dict-item"><b>ΕΥΧΗΝ:</b> Adak olarak...</div>', unsafe_allow_html=True)
    st.markdown('<div class="dict-item"><b>ΕΔΟΞΕΝ:</b> Karar verildi ki...</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Podcast Bölümü
    st.markdown('<div class="info-card" style="text-align:center;">', unsafe_allow_html=True)
    logo_path = "logo.png" if os.path.exists("logo.png") else ("logo.png.png" if os.path.exists("logo.png.png") else None)
    if logo_path:
        st.image(logo_path, width=120)
    st.markdown("""
        <p style="font-size:0.8em; margin-top:10px;"><b>Histofilius Podcast</b></p>
        <a href="https://spotify.com" target="_blank" style="text-decoration:none; color:#8b7355; font-weight:bold; font-size:0.8em;">🎙️ Bölümleri Dinle</a>
    </div>
    """, unsafe_allow_html=True)

with col_main:
    # TAB SİSTEMİ (React'taki gibi)
    tab_analyze, tab_guide = st.tabs(["🔍 Yazıt Analizi", "📜 Epigrafi Rehberi"])
    
    with tab_analyze:
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        # Giriş Yöntemi
        input_method = st.radio("Analiz Yöntemi Seçin:", ["⌨️ Metin Girişi", "📸 Görsel Yükle"], horizontal=True)
        
        if "Metin" in input_method:
            user_input = st.text_area("Yazıt Transkripsiyonunu Girin:", placeholder="Örn: ΕΔΟΞΕΝ ΤΗΙ ΒΟΥΛΗΙ...", height=150)
            image_to_send = None
        else:
            image_to_send = st.file_uploader("Yazıt Fotoğrafı Seçin", type=['png', 'jpg', 'jpeg'])
            if image_to_send:
                st.image(image_to_send, width=400, caption="Analiz edilecek görsel")
            user_input = "Görseldeki yazıtı oku ve analiz et."

        # ANALİZ BUTONU
        if st.button("LABORATUVAR ANALİZİNİ BAŞLAT"):
            if (user_input and "Metin" in input_method) or (image_to_send and "Görsel" in input_method):
                try:
                    # Gemini 2.0 Motoru
                    model = genai.GenerativeModel('gemini-2.0-flash')
                    
                    # Profesör Kişiliği (Prompt)
                    prof_prompt = """Sen Oxford ve Cambridge ekolünden, dünyaca ünlü bir Epigrafi Profesörüsün. 
                    Analizinde şu yapıya sadık kal: 
                    1. Diplomatik Transkripsiyon, 2. Kritik Edizyon, 3. Türkçe Çeviri, 4. Paleografik ve Tarihsel Yorum.
                    Dilin ağırbaşlı, akademik ama merak uyandırıcı olsun."""
                    
                    with st.spinner("Profesör büyüteciyle inceliyor... 🏛️"):
                        if image_to_send:
                            img = Image.open(image_to_send)
                            response = model.generate_content([prof_prompt, user_input, img])
                        else:
                            response = model.generate_content(f"{prof_prompt}\n\nMetin: {user_input}")
                        
                        st.markdown("---")
                        st.subheader("📜 Laboratuvar Bulguları")
                        st.info(response.text)
                        st.balloons()
                except Exception as e:
                    if "429" in str(e):
                        st.error("⚠️ Kota doldu! Profesör 1 dakika çay molası verdi.")
                    else:
                        st.error(f"Teknik bir durum: {e}")
            else:
                st.warning("Lütfen bir metin girin veya görsel yükleyin.")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab_guide:
        st.markdown("""
            <div class="info-card">
                <h3 style="color:#1a2a44; border-bottom: 2px solid #8b7355; padding-bottom: 10px;">🏛️ Epigrafi Rehberi</h3>
                <p><b>Arkaik Dönem:</b> Boustrophedon (öküz dönüşü) yazı stili hakimdir.</p>
                <p><b>Klasik Dönem:</b> Stoikhedon (hizalı) düzen ve mükemmel simetri görülür.</p>
                <p><b>Roma Dönemi:</b> Lunate sigma (C) ve daha kavisli harf formları başlar.</p>
                <hr>
                <p style="font-size:0.8em; font-style:italic;">Bu bilgiler Histofilius Arşivi'nden alınmıştır.</p>
            </div>
        """, unsafe_allow_html=True)

# --- 6. FOOTER ---
st.markdown("<br><p style='text-align:center; opacity:0.5; font-size:0.8em;'>© 2026 EPIGRAPHOS | Klasik Filoloji ve Epigrafi Enstitüsü</p>", unsafe_allow_html=True)
