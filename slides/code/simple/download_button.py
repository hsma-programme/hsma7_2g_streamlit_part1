st.download_button(
    label="Download table as CSV",
    data=underlying.to_csv().encode("utf-8"),
)