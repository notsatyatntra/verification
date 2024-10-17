from langchain_community.llms import Ollama

cached_llm = Ollama(model="llama3", base_url='http://localhost:11434')
