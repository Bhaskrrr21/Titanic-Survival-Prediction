import streamlit as st
import sys

st.title("Testing Environment")

st.write("Python version:", sys.version)

try:
    import joblib
    st.success(f"Joblib imported successfully! Version: {joblib.__version__}")
except Exception as e:
    st.error(f"Error importing joblib: {e}")