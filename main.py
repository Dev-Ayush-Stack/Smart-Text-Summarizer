# importing important packages 
import streamlit as st
from langchain_openai import ChatOpenAI
from io import StringIO
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain


def load_LLM(api_key):
    llm=ChatOpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
        model="openai/gpt-oss-120b",
        temperature=0.0,
    )
    return llm

#Page title and Header
st.set_page_config(page_title="AI Long Text Summarizer")
st.title("AI Long Text Summarizer")

#Intro: instructions
col1,col2=st.columns(2)

with col1:
    st.markdown("Many LLM's like ChatGPT cannot summarize long texts. Now you can do it with this app.")

with col2:
    st.write("Contact with [AP solutions](https://portfolio-sandy-sigma-49.vercel.app/) to build your AI Projects")

# Input API Key 
st.markdown("## Enter Your API Key")

def get_api_key():
    input_text=st.text_input(label="Groq API Key",placeholder="Ex: gsk-2twmA8tfCb8un4...",key="api_key_input",type="password")
    return input_text

api_key=get_api_key()

# Input
st.markdown("## Upload the text file you want to summarize")

upload_file=st.file_uploader("Choose a file",type="txt")

# Output 
st.markdown("###Summarized Content:")

if upload_file is not None:
    #To read files as bytes:
    bytes_data=upload_file.getvalue()
    # st.write(bytes_data)

    # To convert to a string based IO /
    stringio=StringIO(upload_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    string_data=stringio.read()
    # st.write(string_data)

    file_input=string_data

    if file_input:
        if not api_key:
            st.warning('Please insert OpenAI API Key. \
            Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', 
            icon="⚠️")
            st.stop()

    text_splitter=RecursiveCharacterTextSplitter(
        separators=["\n\n","\n"],
        chunk_size=5000,
        chunk_overlap=350
    )

    splitted_documents=text_splitter.create_documents([file_input])
    llm=load_LLM(api_key=api_key)

    summary_chain=load_summarize_chain(
        llm=llm,
        chain_type="map_reduce"
    )

    summary_output=summary_chain.run(splitted_documents)
    st.write(summary_output)