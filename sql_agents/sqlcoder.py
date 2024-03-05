from dotenv import load_dotenv

from langchain_community.llms import HuggingFaceHub
from langchain.schema import (
    HumanMessage,
    SystemMessage,
)
from langchain_community.chat_models.huggingface import ChatHuggingFace

load_dotenv()

# Instantiate LLM
llm = HuggingFaceHub(
    repo_id="defog/sqlcoder-7b-2",
    task="text-generation",
    model_kwargs={
        "max_new_tokens": 512,
        "top_k": 30,
        "temperature": 0.1,
        "repetition_penalty": 1.03,
    },
)

messages = [
    SystemMessage(content="You're a helpful assistant"),
    HumanMessage(
        content="Summarize the top 5 most popular products."
    ),
]

chat_model = ChatHuggingFace(llm=llm)

res = chat_model.invoke(messages)
print(res.content)