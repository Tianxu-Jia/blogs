import streamlit as st
import time 
# Display Streamlit content
st.title("Streamlit App with Gradio Integration")

# Define the Gradio interface
gradio_interface_code = """
from gradio import Interface, Textbox

def greet(name):
    return "Hello, " + name + "!"

iface = Interface(
    fn=greet, 
    inputs=Textbox(label="Name"), 
    outputs="text"
)

iface.launch(share=False)
"""

# Save the Gradio interface code to a Python file
#with open("gradio_interface.py", "w") as file:
#    file.write(gradio_interface_code)

# Start a local server to host the Gradio interface
# Make sure you have Gradio installed (`pip install gradio`) to run this command
import subprocess
aaa = subprocess.Popen(["gradio", "gradio_interface.py"])

# Replace the Gradio interface URL with your generated share link
gradio_interface_url = "http://127.0.0.1:7860/"  # Example URL

# Load the Gradio interface using an iframe
st.write(f'<iframe src="{gradio_interface_url}" width="800" height="600"></iframe>',
         unsafe_allow_html=True)
