# AI Chatbot with Google Gemini, Tavily Search, RAG, and Gradio

An intelligent chatbot that combines:
- **Google GenAI (Gemini)** for language generation  
- **Tavily** for live web search  
- **Hugging Face Transformers** and **Sentence Transformers** for RAG embeddings  
- **Pinecone** as the vector database  
- **LangChain** for orchestration  
- **Gradio** for a clean, interactive frontend  

---

## Getting Started

### Clone the Repository
```bash
git clone https://github.com/Yeetsnake2/AI_ML_Proj1
cd AI_ML_Proj1
```

### Create a conda environment
```bash
conda create chatbot
conda activate chatbot
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Setup environment variables
Create a .env file in the project root with the following contents:
```
GEMINI_API_KEY=YOUR_API_KEY
TAVILY_API_KEY=YOUR_API_KEY
PINECONE_API_KEY=YOUR_API_KEY
```

### Run main.py
```bash
python main.py
```
## Usage note
* Use **Ctrl + C** in the terminal to stop the Gradio server.

