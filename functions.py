from dotenv import load_dotenv
from langchain.llms import OpenAI
import os
import streamlit  as st
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai
load_dotenv()


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, image, prompt):
    model=genai.GenerativeModel("gemini-pro-vision")
    response=model.generate_content([input,image[0],prompt])
    return response.text


def input_image_setup(upload_file):
    if upload_file is not None:
        bytes_data=upload_file.getvalue()

        image_parts=[
            {
                "mime_type":upload_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        FileNotFoundError("No file Uploaded")