import streamlit as st
from generate_report import generate_pdf

st.set_page_config(page_title="Indian Diaspora Report", layout="centered")
st.title("📊 Indian American Economic Impact Report (2025)")

st.markdown("Generate a professional PDF report showing contributions by Indian Americans in the US economy.")

if st.button("📄 Generate Report"):
    pdf_buffer = generate_pdf()
    st.success("✅ PDF successfully generated!")
    st.download_button(
        label="📥 Download Report",
        data=pdf_buffer,
        file_name="Indian_Diaspora_Report_2025.pdf",
        mime="application/pdf"
    )
