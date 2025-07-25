import streamlit as st


from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.documents import Document

# Sidebar for API key
st.sidebar.title("Settings")
openai_api_key = st.sidebar.text_input("Akey", type="password")


# Page title
st.title("📧 Smart Email Writer (RAG-based)")

# Hardcoded internal knowledge base
knowledge_text = """
Our emails should follow a professional and friendly tone. 
- Always begin with a polite greeting.
- Use clear and concise language.
- Include a thank-you or appreciation message where appropriate.
- Add a call-to-action at the end.
- Sign off with name, title, and contact info.
Emails should not sound too robotic or too casual.
"""

# Convert to LangChain document
documents = [Document(page_content=knowledge_text)]

if openai_api_key:
    # Embed knowledge base
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectordb = Chroma.from_documents(documents, embedding=embeddings, persist_directory="db_hardcoded")
    vectordb.persist()

    # Setup QA chain with retrieval
    llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.7)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())

    # Email prompt input
    st.subheader("✍️ What type of email would you like to write?")
    query = st.text_input("e.g., Follow-up email after client meeting")

    if st.button("Generate Email") and query:
        with st.spinner("Generating..."):
            result = qa_chain.run(f"Write a professional email: {query}")
            st.success("Email Generated:")
            st.text_area("📄 Email Output:", result, height=300)
else:
    st.warning("Please enter your OpenAI API key in the sidebar.")
