import streamlit as st
from PIL import Image
import tempfile

# Streamlit page config
st.set_page_config(page_title="Image to PDF Converter", layout="centered")

# Title and description
st.title("🖼️➡️📄 Image to PDF Converter")
st.write("Upload one or more images and convert them into a single PDF file.")

# File uploader
uploaded_files = st.file_uploader(
    "Choose image files", 
    type=["jpg", "jpeg", "png"], 
    accept_multiple_files=True
)

if uploaded_files:
    images = []
    
    # Convert all uploaded images to RGB and store
    for file in uploaded_files:
        try:
            img = Image.open(file).convert("RGB")
            images.append(img)
        except Exception as e:
            st.error(f"❌ Failed to open image: {file.name}. Error: {e}")

    if images and st.button("Convert to PDF"):
        # Create a temporary file to save PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
            images[0].save(tmpfile.name, save_all=True, append_images=images[1:])
            st.success("✅ PDF created successfully!")
            
            # Read and offer download
            with open(tmpfile.name, "rb") as f:
                st.download_button(
                    label="📥 Download PDF",
                    data=f,
                    file_name="converted.pdf",
                    mime="application/pdf"
                )
