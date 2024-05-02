from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat GPTimmy")
    st.header("Chat GPTimmy 💻")

    #uploading file
    pdf = st.file_uploader("Upload your PDF", type="pdf")

    #extracting the text
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        st.write(text)




if __name__ == '__main__':
    main()
