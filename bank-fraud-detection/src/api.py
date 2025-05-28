# app.py

import streamlit as st
import pandas as pd
import os
from src import detector, visualizer, config

st.set_page_config(page_title="Bank Fraud Detection", layout="wide")

st.title("🚨 Bank Fraud Detection System")
st.markdown("Detect and visualize suspicious transactions using ML and network graphs.")

# 🔘 Sidebar Options
option = st.sidebar.selectbox("Choose an Action", ["Run Fraud Detection", "Visualize Money Flow"])

# 🧪 Fraud Detection
if option == "Run Fraud Detection":
    st.subheader("🔍 Run Detection")
    
    if st.button("Run Detection Now"):
        with st.spinner("Running fraud detection..."):
            detector.detect_fraud()
            st.success("✅ Detection Complete!")

        # Load and preview frauds
        if os.path.exists(config.FRAUD_REPORT):
            df = pd.read_csv(config.FRAUD_REPORT)
            st.markdown(f"### 🧾 {len(df)} Suspicious Transactions Found")
            st.dataframe(df.head(20))

            # Download option
            st.download_button(
                label="📥 Download Full Fraud Report (CSV)",
                data=df.to_csv(index=False),
                file_name="fraud_report.csv",
                mime="text/csv"
            )
        else:
            st.warning("Fraud report not found.")

# 🕸️ Graph Visualization
elif option == "Visualize Money Flow":
    st.subheader("📊 Fraud Network Graph")
    st.markdown("This graph shows how money moved between accounts involved in flagged frauds.")
    
    try:
        visualizer.visualize_money_flow(fraud_only=True)
        st.success("✅ Graph rendered below. (Check matplotlib pop-up window)")
    except Exception as e:
        st.error(f"Error: {e}")
