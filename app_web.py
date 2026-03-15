import streamlit as st
import os

# Konfigurasi Halaman
st.set_page_config(
    page_title="Download LitePDF Ultra Pro",
    page_icon="📄",
    layout="centered"
)

# Custom CSS untuk tampilan profesional
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #0078D4;
        color: white;
        font-weight: bold;
    }
    .publisher-box {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.title("🚀 LitePDF Ultra Pro")
st.subheader("El-Syarif Edition")

with st.container():
    st.markdown('<div class="publisher-box">', unsafe_allow_html=True)
    
    # Menampilkan Ikon (Gunakan app_icon.ico jika ada di folder yang sama)
    if os.path.exists("app_icon.ico"):
        st.image("app_icon.ico", width=100)
    
    st.write("### Versi v1.9.0 (Stabil)")
    st.info("Aplikasi Pembaca, Editor, dan Konverter PDF Khusus Lingkungan Pondok Modern Al-Ghozali.")
    
    # Fitur Unggulan
    col1, col2, col3 = st.columns(3)
    col1.metric("Fitur", "Edit Teks")
    col2.metric("Fitur", "Tanda Tangan")
    col3.metric("Fitur", "Konversi")

    # Logika Download File MSI
    msi_file_path = "LitePDF_Ultra_Pro_v1.9.msi"
    
    if os.path.exists(msi_file_path):
        with open(msi_file_path, "rb") as file:
            btn = st.download_button(
                label="📥 UNDUH INSTALLER (.MSI)",
                data=file,
                file_name="LitePDF_Ultra_Pro_v1.9.msi",
                mime="application/octet-stream"
            )
    else:
        st.error("File Installer (.msi) tidak ditemukan di server. Pastikan file ada di folder yang sama.")

    st.markdown("---")
    st.write("**Diterbitkan Oleh:**")
    st.write("### Liyas Syarifudin, S.Pd.I, M.Pd")
    st.caption("© 2026 Al-Ghozali Education Quality Development Institute")
    st.markdown('</div>', unsafe_allow_html=True)

# Panduan Instalasi
with st.expander("ℹ️ Panduan Instalasi"):
    st.write("""
    1. Klik tombol **Unduh** di atas.
    2. Jalankan file `.msi` yang telah diunduh.
    3. Jika muncul peringatan *SmartScreen*, klik 'More Info' lalu 'Run Anyway'.
    4. Selesaikan proses instalasi sampai muncul ikon LitePDF di Desktop Anda.
    """)