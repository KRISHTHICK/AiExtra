import streamlit as st
from pattern_extractor.extract_docx_structure import extract_elements
from pattern_extractor.detect_patterns import detect_common_patterns
from pattern_extractor.pattern_editor import edit_pattern
from pattern_extractor.extractor_engine import extract_data
import json

st.title("🧠 AutoDocPattern-AI")

uploaded_file = st.file_uploader("Upload .docx document", type=["docx"])

if uploaded_file:
    with open("samples/temp.docx", "wb") as f:
        f.write(uploaded_file.read())

    elements = extract_elements("samples/temp.docx")
    patterns = detect_common_patterns(elements)
    approved_pattern = edit_pattern(patterns)

    data = extract_data(elements, approved_pattern)

    st.subheader("Detected Pattern")
    st.json(approved_pattern)

    st.subheader("Extracted Structured Data")
    st.json(data)

    # Save output
    with open("output/patterns.json", "w") as f:
        json.dump(approved_pattern, f, indent=2)
    with open("output/extracted_data.json", "w") as f:
        json.dump(data, f, indent=2)
