import streamlit as st

st.title("🚀 LitePDF Ultra Pro Portal")
st.write("Diterbitkan oleh: **Liyas Syarifudin, S.Pd.I, M.Pd**")

# Link yang Bapak copy dari GitHub Release tadi
url_download = "PASTE_LINK_YANG_DI_COPY_TADI_DISINI"

st.markdown("---")
st.write("Klik tombol di bawah untuk mengunduh installer resmi:")

# Menggunakan link_button agar langsung mengunduh dari server GitHub
st.link_button("📥 UNDUH INSTALLER (.MSI)", url_download, use_container_width=True)

with st.expander("Catatan Rilis v1.9.0"):
    st.write("- Penambahan fitur Edit Teks Profesional (Mode Word)")
    st.write("- Perbaikan sistem navigasi halaman")
    st.write("- Optimasi render teks Arab")
