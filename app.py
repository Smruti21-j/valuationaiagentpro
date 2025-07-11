
import streamlit as st
import pandas as pd
from valuation import run_valuation_model
from report_generator import generate_pdf_report

st.set_page_config(page_title="Valuation AI Agent", layout="wide")
st.title("🧮 Valuation AI Agent – ValServe Corporate Advisors LLP")

with st.sidebar:
    st.header("📝 Report Settings")
    client_name = st.text_input("Client Name", value="Mignesh Global Limited")
    valuation_date = st.date_input("Valuation Date")
    wacc = st.number_input("WACC (%)", min_value=0.0, max_value=100.0, value=12.0)
    terminal_growth = st.number_input("Terminal Growth Rate (%)", min_value=0.0, max_value=10.0, value=4.0)
    projection_years = st.slider("Projection Period (years)", 1, 10, 5)

uploaded_file = st.file_uploader("Upload Financial Excel File (.xlsx)", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.subheader("📊 Uploaded Financial Data")
    st.dataframe(df.head())

    valuation_result = run_valuation_model(df)
    st.subheader("📈 Valuation Summary")
    st.json(valuation_result)

    if st.button("📥 Generate Valuation Report"):
        pdf = generate_pdf_report(
            valuation_result, client_name, valuation_date, wacc, terminal_growth, projection_years
        )
        st.download_button("Download PDF Report", data=pdf, file_name="Valuation_Report.pdf", mime="application/pdf")
