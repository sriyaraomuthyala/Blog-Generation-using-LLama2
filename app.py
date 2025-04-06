import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ['LANGCHAIN_PROJECT'] = 'Blog generation'

# Function to get response from LLama 2 model
def getLLamaresponse(input_text, no_words, blog_style):
    # LLama2 model initialization
    llm = Ollama(model="llama2")

    # Prompt Template
    template = """
    Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words.
    """
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],
                            template=template)

    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    return response

st.set_page_config(page_title="Generate Blogs using LLama2",
                   page_icon="🤖",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Generate Blogs 🤖")
input_text = st.text_input("Enter the Blog Topic")

# Creating columns for additional 2 Fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input("No of words")
with col2:
    blog_style = st.selectbox("Writing the blog for",
                              ('Researchers', 'Creative', 'Common People'), index=0)
submit = st.button("Generate")

# Final Response
if submit:
    if input_text and no_words.isdigit():
        response = getLLamaresponse(input_text, no_words, blog_style)
        st.write(response)
    else:
        st.error("Please enter a valid blog topic and number of words.")
