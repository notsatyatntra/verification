from duckduckgo_search import DDGS

# results = DDGS().text("python programming", max_results=5)
# print(results)

results = DDGS().chat("does Haulier opertae in road transport department in UAE?", model='gpt-4o-mini')
print(results)
