from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2:latest")

template = """
    You are an expert in answering questions about a pizza restaurant.

    Here are some relevant reviews: {reviews}

    Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break

    reviews = retriever.invoke(question)
    reviews_text = "\n\n".join([doc.page_content for doc in reviews])
    result = chain.invoke({"reviews": reviews_text, "question": question})
    print("Result", result)