
# RAG Ask PDF App 

This is a Python application that allows you to load a PDF and ask questions about it using natural language. The application uses a LLM to generate a response about your PDF. The LLM will not answer questions unrelated to the document.

## How it works

The application reads the PDF and splits the text into smaller chunks that can be then fed into a LLM. It uses OpenAI embeddings to create vector representations of the chunks. The application then finds the chunks that are semantically similar to the question that the user asked and feeds those chunks to the LLM to generate a response.

The application uses Streamlit to create the GUI and Langchain to deal with the LLM.
## Installation

To install the repository, please clone this repository and install the requirements:

```bash<img width="960" alt="RAG Capture 3" src="https://github.com/user-attachments/assets/ec67fda9-f6d6-4113-834f-39537ae0712b">

  pip install -r requirements.txt

```
You will also need to add your OpenAI API key to the .env file.

    
## Deployment

To use the application, run the main.py file with the streamlit CLI (after having installed streamlit):


```bash
streamlit run app.py
```
## Screenshots

Once the app is run through streamlit it will look like this:
<img width="960" alt="RAG Capture 3" src="https://github.com/user-attachments/assets/8ccc1445-a610-41d2-8c11-7f9fb53efe47">

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/timmy11803)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/timothy-beta/)
