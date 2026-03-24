import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="EPIGRAPHOS | Antik Yazıt Analiz Laboratuvarı", page_icon="📜", layout="wide")

# API Yapılandırması (Lütfen anahtarın tırnak içinde olduğundan emin ol)
API_KEY = API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

# 🎨 AKADEMİK VE PROFESYONEL TASARIM (CSS)
st.markdown("""
    <style>
    /* Üst Lacivert Band */
    .header-band {
        background-color: #1a2a3a;
        padding: 30px;
        border-radius: 0 0 15px 15px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 30px;
    }
    .header-title { font-family: 'Georgia', serif; font-size: 42px; letter-spacing: 2px; margin: 0; }
    .header-subtitle { font-size: 14px; letter-spacing: 3px; color: #bdc3c7; text-transform: uppercase; }
    .quote-text { font-size: 18px; color: #f1c40f; font-style: italic; }

    /* Kartlar */
    .info-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #1a2a3a;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        height: 200px;
    }
    .card-title { color: #1a2a3a; font-family: 'Georgia', serif; font-size: 22px; margin-bottom: 15px; border-bottom: 1px solid #eee; }

    /* Spotify Butonu Özelleştirme */
    .spotify-btn {
        background-color: #1DB954;
        color: white !important;
        padding: 15px 25px;
        text-decoration: none;
        border-radius: 30px;
        font-weight: bold;
        display: inline-flex;
        align-items: center;
        gap: 10px;
        margin-top: 20px;
        transition: 0.3s;
    }
    .spotify-btn:hover { background-color: #1ed760; transform: scale(1.05); }

    /* Metin Alanı */
    .stTextArea>div>div>textarea { background-color: #fdfcf9; border: 1px solid #d1d1d1; font-size: 1.1em; }
    </style>
    """, unsafe_allow_html=True)

# 🏛️ ÜST BAND
st.markdown("""
    <div class="header-band">
        <div>
            <h1 class="header-title">EPIGRAPHOS</h1>
            <p class="header-subtitle">ANTİK YUNAN YAZIT ANALİZ LABORATUVARI</p>
        </div>
        <div style="text-align: right;">
            <p class="quote-text">"Scripta manent, verba volant."</p>
            <p style="font-size: 12px; color: #bdc3c7;">Oxford Classics / Epigraphy Dept.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 📜 BİLGİ KARTLARI VE SPOTIFY
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("""
        <div class="info-card">
            <div class="card-title">⚒️ Metodoloji</div>
            <ul style="list-style-type: none; padding-left: 0; font-size: 0.9em;">
                <li>> Leiden Konvansiyonu kullanımı</li>
                <li>> Paleografik karşılaştırma</li>
                <li>> Onomastik veritabanı taraması</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="info-card">
            <div class="card-title">📖 Sıkça Kullanılanlar</div>
            <p style="color: #2980b9; font-weight: bold; font-size: 0.8em; margin-bottom: 5px;">MEZAR YAZITLARI</p>
            <code style="display: block; background: #f4f4f4; padding: 5px; font-size: 0.8em;">ΕΝΘΑΔΕ ΚΕΙΤΑΙ (Burada yatıyor...)</code>
        </div>
        """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="info-card" style="text-align: center; border-left: 5px solid #1DB954;">
            <div class="card-title" style="color: #1DB954;">🎙️ Podcast</div>
            <p style="font-size: 0.9em;">Geç Cumhuriyet Dönemi'ni keşfedin.</p>
            <a href="https://open.spotify.com/show/5R1Y05N92i8U2W6YI8vVzG" target="_blank" class="spotify-btn">
                <span>Spotify'da Dinle</span>
            </a>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# ✍️ ANALİZ ALANI
st.subheader("🖋️ Analiz Edilecek Metni Girin")
input_text = st.text_area("", placeholder="Analiz edilecek yazıtı buraya yapıştırın...", height=150)
if st.button("ANALİZİ BAŞLAT", use_container_width=True):
    if input_text:
        with st.spinner("Profesör kütüphaneden geliyor... 🏛️"):
            try:
                # Modeli 'models/' ön ekiyle çağırıyoruz ki v1beta hatası sussun
                model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
                
                prompt = f"""
                Sen uzman bir epigrafistsin. Aşağıdaki antik metni analiz et:
                Metin: {input_text}
                
                Lütfen şu formatta cevap ver:
                1. Transkripsiyon (Grekçe/Latince)
                2. Türkçe Çeviri
                3. Tarihsel ve Epigrafik Yorum
                """
                
                response = model.generate_content(prompt)
                
                st.success("Analiz Tamamlandı!")
                st.markdown("### 📜 Profesörün Notları")
                st.info(response.text) 
                
            except Exception as e:
                if "429" in str(e):
                    st.error("⚠️ Kota doldu. 1 dakika sonra tekrar deneyin.")
                else:
                    st.error(f"Teknik bir durum: {e}")
                
            except Exception as e:
                if "429" in str(e):
                    st.error("⚠️ Google Ücretsiz Kotası Doldu. Lütfen 1-2 dakika bekleyip tekrar deneyin. (Profesör çay molasında ☕)")
                else:
                    st.error(f"Teknik bir aksaklık: {e}")
    else:
        st.warning("Lütfen analiz edilecek bir metin girin.")

                    

# 🏷️ FOOTER
st.markdown("<p style='text-align: center; color: gray; margin-top: 50px;'>Histofilius Digital Heritage Project © 2026</p>", unsafe_allow_html=True)
