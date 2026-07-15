import streamlit as st
import sys
import subprocess

st.title("Environment Check")

st.write("Python:", sys.version)

result = subprocess.run(
    [sys.executable, "-m", "pip", "list"],
    capture_output=True,
    text=True,
)

st.text(result.stdout)