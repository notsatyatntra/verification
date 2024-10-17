from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.document_loaders import PDFPlumberLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

cached_llm = Ollama(model="llama3")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1024, chunk_overlap=80, length_function=len, is_separator_regex=False
)

raw_prompt = PromptTemplate.from_template(
    """ 
    <s>[INST] You are a technical assistant good at searching docuemnts. If you do not have an answer from the provided information say so. [/INST] </s>
    [INST] {input}
           Context: {context}a
           Answer:
    [/INST]
"""
)
loader=PyPDFLoader("pdf_files_new/website_1.pdf")
pages=loader.load_and_split()
pages

from langchain.schema import Document
from langchain_community.vectorstores import DocArrayInMemorySearch

vector_store=DocArrayInMemorySearch.from_documents(
    pages,
    embedding=embeddings
)

print("Creating chain")
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={
        "k": 20,
        "score_threshold": 0.1,
    },
)

document_chain = create_stuff_documents_chain(cached_llm, raw_prompt)
chain = create_retrieval_chain(retriever, document_chain)
query = "What is the work of Agility Logistics company?"
result = chain.invoke({"input": query})

print(result)













































































































# chat_history = []
# query = ""
# folder_path = "/home/tntra/Documents/verification/pdf_files_new"
# vector_store = Chroma(persist_directory=folder_path, embedding_function=embedding)

# retriever = vector_store.as_retriever(
#         search_type="similarity_score_threshold",
#         search_kwargs={
#             "k": 20,
#             "score_threshold": 0.1,
#         },
#     )

# retriever_prompt = ChatPromptTemplate.from_messages(
#     [
#         MessagesPlaceholder(variable_name="chat_history"),
#         ("human", "{input}"),
#         (
#             "human",
#             "Given the above conversation, generation a search query to lookup in order to get information relevant to the conversation",
#         ),
#     ]
# )

# history_aware_retriever = create_history_aware_retriever(
#     llm=cached_llm, retriever=retriever, prompt=retriever_prompt
# )

# document_chain = create_stuff_documents_chain(cached_llm, raw_prompt)
# # chain = create_retrieval_chain(retriever, document_chain)

# retrieval_chain = create_retrieval_chain(
#     # retriever,
#     history_aware_retriever,
#     document_chain,
# )

# result = retrieval_chain.invoke({"input": query})
# print(result["answer"])
# chat_history.append(HumanMessage(content=query))
# chat_history.append(AIMessage(content=result["answer"]))

# sources = []
# for doc in result["context"]:
#     sources.append(
#         {"source": doc.metadata["source"], "page_content": doc.page_content}
#     )

# response_answer = {"answer": result["answer"], "sources": sources}
