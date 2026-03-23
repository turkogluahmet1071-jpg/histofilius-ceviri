import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# --- YAPILANDIRMA VE ANAHTAR ---
# Buraya kendi Gemini API anahtarını koymalısın
API_KEY = "AIzaSyBpuXwhUlhXcRd4eZ9Sp4uIL4LKfYsN8pg" 
genai.configure(api_key=API_KEY)

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="EPIGRAPHOS | Histofilius", page_icon="🏛️", layout="wide")

# Antik Tasarım (CSS)
st.markdown("""
    <style>
    .main { background-color: #fcfaf2; }
    .stButton>button { background-color: #8b7355; color: white; border-radius: 10px; font-weight: bold; }
    h1, h2, h3 { color: #1a2a44; font-family: 'serif'; }
    .sidebar .sidebar-content { background-color: #1a2a44; color: #e5d5b0; }
    </style>
    """, unsafe_allow_html=True)

# --- SİSTEM KOMUTU (Senin React kodundaki profesör) ---
SYSTEM_PROMPT = """
Sen Oxford ve Cambridge ekolünden gelen, dünyaca ünlü bir Klasik Filolog ve Epigrafi Profesörüsün. 
Görevin: Kullanıcının sağladığı Antik Yunan yazıtını (metin veya görsel) en yüksek akademik titizlikle analiz etmek.

Analizinde şu yapıya sadık kal:
1. **Diplomatik Transkripsiyon**: Orijinal yazımdaki harf formlarını koruyarak metni dök.
2. **Kritik Edizyon**: Eksik kısımları [] parantezleri ile tamamla.
3. **Türkçe Çeviri**: Akıcı ve doğru bir çeviri.
4. **Paleografik Analiz**: Tarihlendirme tahmini.
5. **Tarihsel ve Sosyal Bağlam**: Dönem hakkında ne anlatıyor?

Dilin ağırbaşlı, akademik ama merak uyandırıcı olsun.
"""

# --- UI BAŞLIK ---
st.markdown("<h1 style='text-align: center;'>🏛️ EPIGRAPHOS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>Antik Yunan Yazıt Analiz Laboratuvarı</p>", unsafe_allow_html=True)
st.divider()

# --- SIDEBAR (Rehber Bölümü) ---
with st.sidebar:
    st.title("📜 Metodoloji")
    st.info("Leiden Konvansiyonu kullanımı ve Paleografik karşılaştırma esas alınır.")
    st.divider()
    st.write("🎙️ **divi filius** Podcast")
    st.write("📺 **Histofilius** YouTube")

# --- ANA İÇERİK ---
col1, col2 = st.columns([1, 1])

with col1:
    tab1, tab2 = st.tabs(["⌨️ Metin Girişi", "📸 Görsel Yükle"])
    
    with tab1:
        text_input = st.text_area("Yazıt Transkripsiyonu:", placeholder="Örn: ΕΔΟΞΕΝ ΤΗΙ ΒΟΥΛΗΙ...", height=200)
    
    with tab2:
        uploaded_file = st.file_uploader("Yazıt Fotoğrafı Seçin", type=['png', 'jpg', 'jpeg'])
        if uploaded_file:
            st.image(uploaded_file, caption="Yüklenen Yazıt", use_container_width=True)

    analyze_btn = st.button("🔍 Yazıtı Analiz Et", use_container_width=True)

with col2:
    if analyze_btn:
        model = genai.GenerativeModel('gemini-1.5-pro', system_instruction=SYSTEM_PROMPT)
        
        try:
            with st.spinner("Profesör parşömenleri inceliyor..."):
                if uploaded_file:
                    img = Image.open(uploaded_file)
                    response = model.generate_content(["Bu görseldeki yazıtı analiz et.", img])
                else:
                    response = model.generate_content(f"Şu metni analiz et: {text_input}")
                
                st.markdown("### 📜 Laboratuvar Bulguları")
                st.write(response.text)
                st.success("Analiz Tamamlandı.")
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")
    else:
        st.info("Analiz sonuçları burada görünecek. Soldan bir giriş yapıp butona basın.")
