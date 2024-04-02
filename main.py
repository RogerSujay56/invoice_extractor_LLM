from dotenv import load_dotenv
from langchain.llms import OpenAI
import os
import streamlit  as st
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai
from functions import *
load_dotenv()


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


st.set_page_config(page_title="Invoice Reader LLM")
st.header("Gemini Application")
input=st.text_input("Input Prompts: ",key="input")
upload_file=st.file_uploader(label="Choose an Image...",type=["jpg","jpeg","png"])
image=""
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption="uploaded image",use_column_width=True)


submit=st.button("Ask Me?")

input_prompt="""
                you are an expert in understanding invoices machine printed as well as handwritten.
                you will receive input images as invoices and you will have to answer the questions based on input image.
                """


if submit:
    image_data=input_image_setup(upload_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)