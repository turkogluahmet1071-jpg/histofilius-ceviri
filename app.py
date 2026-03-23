import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="EPIGRAPHOS | Antik Yazıt Analiz Laboratuvarı", page_icon="📜", layout="wide")

# 🎨 AKADEMİK TASARIM (CSS)
st.markdown("""
    <style>
    /* Üst Başlık Bandı (Lacivert) */
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
    .header-title {
        font-family: 'Georgia', serif;
        font-size: 42px;
        letter-spacing: 2px;
        margin: 0;
    }
    .header-subtitle {
        font-size: 14px;
        letter-spacing: 3px;
        color: #bdc3c7;
        text-transform: uppercase;
    }
    .quote-section {
        text-align: right;
        font-style: italic;
    }
    .quote-text { font-size: 18px; color: #f1c40f; }
    .quote-source { font-size: 12px; color: #bdc3c7; }

    /* Kart Tasarımları (Metodoloji ve Sıkça Kullanılanlar) */
    .info-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #1a2a3a;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .card-title {
        color: #1a2a3a;
        font-family: 'Georgia', serif;
        font-size: 22px;
        margin-bottom: 15px;
        border-bottom: 1px solid #eee;
    }
    
    /* Metin Alanı Özelleştirme */
    .stTextArea>div>div>textarea {
        background-color: #fdfcf9;
        border: 1px solid #d1d1d1;
    }
    </style>
    """, unsafe_allow_html=True)

# 🏛️ ÜST BANDI OLUŞTUR
st.markdown("""
    <div class="header-band">
        <div>
            <h1 class="header-title">EPIGRAPHOS</h1>
            <p class="header-subtitle">ANTİK YUNAN YAZIT ANALİZ LABORATUVARI</p>
        </div>
        <div class="quote-section">
            <p class="quote-text">"Scripta manent, verba volant."</p>
            <p class="quote-source">Oxford Classics / Epigraphy Dept.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 📜 ANA İÇERİK (SOL VE SAĞ KOLON)
col1, col2 = st.columns([1, 1])

with col1:
    # 🛠️ METODOLOJİ BÖLÜMÜ
    st.markdown("""
        <div class="info-card">
            <div class="card-title">⚒️ Metodoloji</div>
            <ul style="list-style-type: none; padding-left: 0;">
                <li>> Leiden Konvansiyonu kullanımı</li>
                <li>> Paleografik karşılaştırma</li>
                <li>> Onomastik veritabanı taraması</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with col2:
    # 📖 SIKÇA KULLANILANLAR BÖLÜMÜ
    st.markdown("""
        <div class="info-card">
            <div class="card-title">📖 Sıkça Kullanılanlar</div>
            <p style="color: #2980b9; font-weight: bold; margin-bottom: 5px;">MEZAR YAZITLARI</p>
            <code style="background-color: #f4f4f4; padding: 5px; border-radius: 5px; display: block;">
                ΕΝΘΑΔΕ ΚΕΙΤΑΙ (Burada yatıyor...)
            </code>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# ✍️ ANALİZ ALANI
st.subheader("🖋️ Analiz Edilecek Metni Girin")
input_text = st.text_area("", placeholder="Örn: ΣΩΚΡΑΤΗΣ ΕΝ ΑΘΗΝΑΙΣ", height=120)

if st.button("ANALİZİ BAŞLAT"):
    if input_text:
        st.info("⚠️ Profesör şu an kütüphanede (Gemini 404). Akademik arayüz başarıyla yüklendi!")
    else:
        st.warning("Lütfen bir metin girin.")

# 🏷️ FOOTER
st.markdown("<p style='text-align: center; color: gray; margin-top: 50px;'>Histofilius Digital Heritage Project © 2026</p>", unsafe_allow_html=True)            
