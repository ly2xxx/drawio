import streamlit as st
# import base64
import xml.etree.ElementTree as ET
from io import BytesIO
# from python_drawio.drawio import DrawioFile
# import drawpyo
# from drawpyo.diagram import Diagram
from drawioedit import DrawIOEdit
import tempfile
import os
import zlib 
import base64 
import png
import re
from PIL import Image
import io

def extract_drawio_xml(png_filename):
    with open(png_filename, 'rb') as f:
        img_data = f.read()

    # Load the image using PIL to get the text chunks
    img = Image.open(io.BytesIO(img_data))
    
    # Extract text chunks from the PNG
    for chunk in img.info.get('text', []):
        if chunk.startswith('mxfile'):
            # Extract the base64 encoded part
            encoded_data = chunk.split('%3C')[1]
            # Fix padding by adding '=' characters
            while len(encoded_data) % 4 != 0:
                encoded_data += '='
            try:
                compressed_data = base64.b64decode(encoded_data)
                xml_data = zlib.decompress(compressed_data, -zlib.MAX_WBITS).decode('utf-8')
                return xml_data
            except Exception as e:
                print(f"Error decoding: {e}")
                return None

# def extract_drawio_xml(png_filename):
#     reader = png.Reader(png_filename)
#     for chunk_type, chunk_data in reader.chunks():
#         if chunk_type == b'tEXt':
#             text_data = chunk_data.decode('latin1')
#             if text_data.startswith('mxfile'):
#                 compressed_data = base64.b64decode(text_data.split('%3C')[1])
#                 xml_data = zlib.decompress(compressed_data, -zlib.MAX_WBITS).decode('utf-8')
#                 return xml_data
            
# def extract_drawio_xml(png_file):
#     # Read the PNG file in binary mode
#     content = png.Reader(png_file) #png_file.read()
    
#     # Look for the Draw.io XML data in PNG chunks
#     xml_start = content.find(b'mxfile')
#     if xml_start != -1:
#         # Extract the compressed data
#         compressed_data = content[xml_start:]
#         # Find the end of the XML data
#         xml_end = compressed_data.find(b'IEND')
#         if xml_end != -1:
#             compressed_data = compressed_data[:xml_end]
            
#         # Clean and decode the data
#         try:
#             # Remove any PNG chunk headers
#             clean_data = re.sub(b'[0-9a-fA-F]{8}', b'', compressed_data)
#             # Decompress if needed
#             try:
#                 xml_data = zlib.decompress(clean_data)
#             except:
#                 xml_data = clean_data
                
#             return xml_data.decode('utf-8')
#         except Exception as e:
#             return f"<mxfile><diagram>Unable to extract XML: {str(e)}</diagram></mxfile>"
    
#     return "<mxfile><diagram>No Draw.io XML data found</diagram></mxfile>"

base_path=os.path.dirname(os.path.realpath(__file__))
png_file = f'{base_path}/c4-icons.drawio.png'
xml_output = extract_drawio_xml(png_file)
print(xml_output)

# Function to convert XML to string
def xml_to_string(xml_data):
    return ET.tostring(xml_data, encoding='utf-8').decode('utf-8')

# Function to process uploaded file
def process_file(uploaded_file):
    # Simulate extracting XML from the file
    # This should be replaced with actual extraction logic
    return f'<mxfile host="app.diagrams.net" version="24.9.0"><diagram id="dummyId" name="Page-1"><root></root></diagram></mxfile>'

# Streamlit application layout
st.title("Draw.io Diagram Editor")

base_path=os.path.dirname(os.path.realpath(__file__))
drawing=DrawIOEdit(file_path=f'{base_path}/c4.drawio.modified.drawio')
print(drawing.xml)


# File uploader
uploaded_file = st.file_uploader("Upload Draw.io Bitmap", type=["png", "jpg", "jpeg", "svg"])

# Placeholder for image and XML
# if uploaded_file is not None:
#     # Create a BytesIO object from the uploaded file
#     file_bytes = BytesIO(uploaded_file.read())
    
#     # Use DrawioFile to extract XML
#     editor = DrawioEditor(file_bytes)
#     xml_data = editor.get_xml()
    
#     # Display image and XML
#     st.image(uploaded_file, caption='Uploaded Draw.io Diagram', use_column_width=True)
#     xml_text = st.text_area("XML Representation", value=xml_data, height=300)
    
#     # Enable two-way sync
#     if xml_text != xml_data:
#         try:
#             # Update the diagram with new XML
#             editor.set_xml(xml_text)
#             # Generate new PNG
#             new_png = editor.to_png()
#             st.image(new_png, caption='Updated Diagram', use_column_width=True)
#         except Exception as e:
#             st.error(f"Failed to update diagram: {str(e)}")
if uploaded_file is not None:
    # Save uploaded file to temporary location with .svg extension since DrawIOEdit expects SVG
    with tempfile.NamedTemporaryFile(delete=False, suffix='.drawio.svg') as tmp_file:
        # Convert PNG to SVG format first
        tmp_file.write(uploaded_file.getvalue())
        temp_path = tmp_file.name
    
    # Use DrawIOEdit with SVG file path
    editor = DrawIOEdit(temp_path)
    xml_data = editor.get_xml()
    
    # Display image and XML
    st.image(uploaded_file, caption='Uploaded Draw.io Diagram', use_column_width=True)
    xml_text = st.text_area("XML Representation", value=xml_data, height=300)
    
    # Enable two-way sync
    if xml_text != xml_data:
        try:
            editor.set_xml(xml_text)
            new_svg_path = os.path.join(tempfile.gettempdir(), 'output.drawio.svg')
            editor.save(new_svg_path)
            st.success("Diagram updated successfully!")
        except Exception as e:
            st.error(f"Failed to update diagram: {str(e)}")
            
    # Cleanup temporary files
    os.unlink(temp_path)
    if 'new_svg_path' in locals():
        os.unlink(new_svg_path)
else:
    xml_text = st.text_area("XML Representation", value="Upload a Draw.io bitmap to extract XML.", height=300)

# Two-way synchronization (simplified)
if st.button("Update XML"):
    # Update XML based on text area input
    xml_data = xml_text
    st.success("XML updated!")

if st.button("Update Image"):
    # In a real application, you would convert the XML back to an image
    st.warning("Image update functionality is not implemented yet!")

# Footer
st.markdown("""
    <style>
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)