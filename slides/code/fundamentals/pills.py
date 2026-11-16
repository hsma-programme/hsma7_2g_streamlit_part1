import streamlit as st

st.pills(
    label="Choose an option",
    options=["A", "B", "C"],
    default="A",
)

st.segmented_control(
    label="Choose an option",
    options=["A", "B", "C"],
    default="A",
)
