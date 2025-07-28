AutoDocPattern-AI/
├── app.py                      # Streamlit App
├── pattern_extractor/
│   ├── extract_docx_structure.py  # Extracts styles, tables, colors, boxes
│   ├── detect_patterns.py         # Detects layout patterns automatically
│   ├── pattern_editor.py          # Simulates human-in-the-loop editing
│   └── extractor_engine.py        # Applies final pattern to extract data
├── samples/
│   └── complex_sample.docx        # Complex test document
├── output/
│   ├── patterns.json              # Saved patterns from document
│   └── extracted_data.json        # Final extracted structured data
└── requirements.txt
