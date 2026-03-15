import streamlit as st

st.set_page_config(page_title="LitePDF Download", page_icon="📄")

st.title("🚀 LitePDF Ultra Pro")
st.subheader("El-Syarif Edition")

# GANTI LINK DI BAWAH INI dengan link yang Bapak Copy dari Github Release
url_rilis = "https://github.com/liyas-syarifudin/NAMA_REPO_BAPAK/releases/download/v1.9.0/LitePDF_Ultra_Pro_v1.9.msi"

st.info("Aplikasi Pembaca & Editor PDF Khusus Pondok Modern Al-Ghozali")

# Gunakan link_button, BUKAN download_button
st.link_button("📥 UNDUH INSTALLER (.MSI)", url_rilis, use_container_width=True)

st.markdown("---")
st.caption("Diterbitkan oleh: Liyas Syarifudin, S.Pd.I, M.Pd")
