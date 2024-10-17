import ollama
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from semantic_router.utils.function_call import FunctionSchema

llm = "llama3.1"
q = '''does Haulier opertae in road transport department in UAE?
        NOTE: Just give me a yes or no'''

# res = ollama.chat(model=llm, 
#                   messages=[{"role":"system", "content":""},
#                             {"role":"user", "content":q}])
# print(res)

@tool("tool_browser")
def tool_browser(q: str) -> str:
    """Search on DuckDuckGo browser by passing the input `q`"""
    return DuckDuckGoSearchRun().run(q)

# test

def browser(q:str) -> str:
    """Search on DuckDuckGo browser by passing the input `q`"""
    return DuckDuckGoSearchRun().run(q)

tool_browser = FunctionSchema(browser).to_ollama()
print(tool_browser)
